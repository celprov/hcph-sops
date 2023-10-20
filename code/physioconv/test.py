import re
import pandas as pd

TRIAL_TYPE = {
    "bh_body_2": "hold",
    "bh_body": "hold-test",
    "bh_end": "hold-end-test",
    "bh_end_2": "hold-end",
    "bh_end_3": "breath-freely",
    "eye_movement_fixation": "cog",
    "ft_hand": "mot",
    "fixation": "blank",
    "grating": "vis",
    "movie": "movie",
    "polygon_4": "breath-in",
    "polygon_5": "breath-out",
    "polygon_6": "breath-in-last",
    "polygon_8": "breath-out-last",
    "polygon_7": "breath-out-last",
}

file = """
62.3562 	EXP 	text_2: autoDraw = True
100.7936 	DATA 	Keypress: s
100.8108 	EXP 	text_2: autoDraw = False
100.8108 	EXP 	directions: autoDraw = True
102.3922 	DATA 	Keypress: s
281.6250 	EXP 	Imported xpos_ypos.csv as conditions, 6 conditions, 2 params
281.6253 	EXP 	Created sequence: random, trialTypes=6, nReps=1, seed=None
281.6255 	EXP 	New trial (rep=0, index=0): OrderedDict([('xpos', -0.7), ('ypos', 0.0)])
281.6300 	EXP 	grating: autoDraw = False
281.6300 	EXP 	polygon: autoDraw = False
281.6300 	EXP 	grating: autoDraw = False
281.6300 	EXP 	polygon: autoDraw = False
281.6300 	EXP 	eye_movement_fixation: autoDraw = True
281.6300 	EXP 	eye_movement_fixation_inner: autoDraw = True
"""

trigger_pattern = r"([\d.]+)\s+DATA\s+Keypress:\s+s"
trigger_match = float(re.findall(trigger_pattern, file)[0])

print(trigger_match)

log = "/home/cprovins/data/hcph-pilot/Psychopy_organized/session-2023-07-14/control_task_1_FINAL_2023-07-14_18h27.05.674.log"

with open(log, "r") as f:
    file = f.read()
    event_dataframe = pd.DataFrame(columns=["onset", "duration", "trial-type", "value"])

    # Find the timestamp of the first trigger aka the beginning of fMRI recording
    trigger_pattern = r"([\d.]+)\s+DATA\s+Keypress:\s+s"
    trigger_timestamp = float(re.findall(trigger_pattern, file)[0])

    # Create a regular expression pattern to match lines containing any of the word corresponding to tasks
    autodraw_pattern = r"([\d.]+)\s+EXP\s+({}):\s+autoDraw\s*=\s*(\w+)".format(
        "|".join(TRIAL_TYPE.keys())
    )

    # Use re.findall to find all matching lines in the log
    autodraw_events = re.findall(autodraw_pattern, file)

    # Initialize variable to keep track of the start timestampss
    start_timestamp = {}

    # Extract the times associated with the matches
    if autodraw_events:
        for timestamp, keyword, status in autodraw_events:
            if status == "True":
                # Store the start timestamp for "autoDraw=False"
                start_timestamp[keyword] = timestamp

            elif status == "False" and keyword in start_timestamp:

                # Calculate the duration for "autoDraw=False" if there is a corresponding "autoDraw=True"
                onset = float(start_timestamp[keyword])
                end = float(timestamp)
                duration = end - onset

                trial_type = TRIAL_TYPE[keyword]

                # For the fingertapping and the eye movement sub-tasks, we have to encode which hand or the position
                # of the fixation point to fully characterize the task instance.
                value = ""
                if trial_type == "mot":
                    hand_pattern = (
                        r"{:.4f}\s+EXP\s+ft_hand:\s*text\s*=\s*\'(RIGHT|LEFT)\'".format(
                            onset
                        )
                    )
                    hand_match = re.search(hand_pattern, file)
                    value = hand_match.group(1).lower()
                elif trial_type == "cog":
                    # The position of the point is reported in the psychopy log 5 to 7 lines above
                    # the onset event of the cognitive instance.

                    # Retrieve line number corresponding to the onset event
                    pattern = r"{:.4f}\s+EXP\s+{}:\s+autoDraw\s*=\s*True".format(
                        onset, keyword
                    )
                    match = re.search(pattern, file)
                    (
                        start,
                        end,
                    ) = match.span()  # Get the start and end position of the match
                    line_nbr = (
                        file.count("\n", 0, start) + 1
                    )  # Calculate the corresponding line number

                    # Search for the capture pattern within seven lines before the match
                    previous_lines = file.split("\n")[line_nbr - 7 : line_nbr]
                    previous_lines_text = "\n".join(previous_lines)

                    fix_pos_pattern = r"([\d.]+)\s+EXP\s+New trial \(rep=\d+, index=\d+\): OrderedDict\(\[\(\'xpos\', (-?\d+\.\d+)\), \(\'ypos\', (-?\d+\.\d+)\)\]\)"

                    # Find all the matches using the regular expression
                    matches = re.findall(fix_pos_pattern, previous_lines_text)
                    # There should be only one match, otherwise we risk mixing up different instances
                    assert len(matches) == 1
                    timestamp, xpos, ypos = matches[0]
                    value = f"[{xpos}, {ypos}]"

                # If no trigger were recorded in the psychopy log, we need to approximate its timestamp
                # with the closest log event.
                if not timestamp:
                    if keyword == "movie":
                        # We coded the resting-state task such that the movie starts at the trigger.
                        trigger_timestamp = onset
                    elif keyword in ["blank", "cog", "mot", "cog"]:
                        # The closest event for qct is "EXP 	eyetracker.clearEvents()"
                        trigger_pattern = r"(\d+\.\d+)\s+EXP\s+eyetracker.clearEvents()"
                        trigger_timestamp = float(re.findall(trigger_pattern, file)[0])
                    else:
                        # The closest event for bht is "EXP  text_2: autoDraw = False"
                        trigger_pattern = r"(\d+\.\d+)\s+EXP\s+text_2: autoDraw = False"
                        trigger_timestamp = float(re.findall(trigger_pattern, file)[0])

                # Subtract the timestamp of the first trigger to the onset of the task to get events
                # onset in the fMRI recording time.
                onset = onset - trigger_timestamp

                # Keep only 1 decimal of precision
                onset = round(onset, 1)
                duration = round(duration, 1)

                # We have all the information needed for the event, it can be inserted in the dataframe.
                event = {
                    "onset": onset,
                    "duration": duration,
                    "trial-type": trial_type,
                    "value": value,
                }
                event_dataframe = pd.concat(
                    [event_dataframe, pd.DataFrame([event])], ignore_index=True
                )

                # Remove the start timestamp from the dictionary to avoid double counting
                del start_timestamp[keyword]

        print(event_dataframe.to_string())

    else:
        print("No match")
"""
log = "/home/cprovins/data/hcph-pilot/Psychopy_organized/session-2023-07-14/control_task_1_FINAL_2023-07-14_18h27.05.674.log"

from write_event_file import write_event_file_from_log

event_df = write_event_file_from_log(log)
print(event_df)
"""
