# Copyright 2023 The Axon Lab <theaxonlab@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# We support and encourage derived works from this project, please read
# about our expectations at
#
#     https://www.nipreps.org/community/licensing/
#
import argparse
import pandas as pd
import os
import gzip
import json
import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import unittest

EVENTS_JSON_BOILERPLATE = {
    "StimulusPresentation": {
        "OperatingSystem": "Linux Ubuntu 20.04.5",
        "SoftwareName": "PsychoPy",
        "SoftwareRRID": "SCR_006571",
        "SoftwareVersion": "2022.3.0.dev6",
    }
}

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


class PatternNotFoundError(Exception):
    def __init__(self, pattern, log):
        super().__init__(
            f"The pattern {pattern} was not found in the log. Please check that the input {log} is a log output by Psychopy and that it does not correspond to a task that was aborted."
        )


def plot_physio_data_with_events(
    time_series_df: pd.DataFrame,
    events_df: pd.DataFrame,
    tsv_file: str,
    output_folder: str = ".",
) -> str:
    """
    Plot physiological data along with events.

    Parameters
    ----------
    time_series_df : :obj:`pandas.DataFrame`
        Table containing the physiological data.
    events_df : :obj:`pandas.DataFrame`
        Table containing the event data.
    tsv_file : :obj:`os.pathlike`
        Path to the TSV file.
    output_folder : :obj:`os.pathfile`
        Output folder for saving the plot image. Default is current directory.

    Returns
    -------
    The path where the plot was saved as a PNG file.

    """
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(30, 10), sharex=True)
    ax1.plot(time_series_df[0], time_series_df[1], label="RB")
    ax2.plot(time_series_df[0], time_series_df[2], label="ECG")
    ax3.plot(time_series_df[0], time_series_df[3], label="GA")
    trial_types = events_df["trial-type"].unique()
    legend_colors = plt.cm.get_cmap("Set1", len(trial_types))
    legend_color_dict = {
        trial_type: legend_colors(i) for i, trial_type in enumerate(trial_types)
    }
    color_patches = []

    for trial_type in trial_types:
        legend_color = legend_color_dict[trial_type]
        color_patch = mpatches.Patch(color=legend_color, label=trial_type)
        color_patches.append(color_patch)
        events_of_type = events_df[events_df["trial-type"] == trial_type]

        for index, row in events_of_type.iterrows():
            ax1.axvline(row["onset"], color=legend_color, linestyle="--")
            ax2.axvline(row["onset"], color=legend_color, linestyle="--")
            ax3.axvline(row["onset"], color=legend_color, linestyle="--")
    ax1.set_ylabel("V")
    ax2.set_ylabel("V")
    ax3.set_ylabel("V")
    ax3.legend(handles=color_patches, loc="lower right")
    ax1.set_title("RB")
    ax2.set_title("ECG")
    ax3.set_title("GA")
    base_name = os.path.basename(tsv_file)
    output_file = os.path.join(
        output_folder, base_name.replace("_physio.tsv.gz", "_plot.png")
    )
    plt.tight_layout()
    plt.savefig(output_file)
    return output_file


def write_event_file_from_channels(tsv_file: str) -> None:
    """
    Create a BIDS events file from the digital channels of the physiological file.

    Parameters
    ----------
    tsv_file :obj:`os.pathlike`
         The path to the input gzipped TSV file containing physiological data of a task.

    """
    with gzip.open(tsv_file, "rt") as file:
        df = pd.read_csv(file, sep="\t", header=None)
    event_dataframe = pd.DataFrame(columns=["onset", "duration", "trial-type"])
    if "bht" in tsv_file:
        for index, row in df.iterrows():
            if row[6] == 5:
                breathin = {"onset": row[0], "duration": 2.7, "trial-type": "breath-in"}
                breathout = {
                    "onset": row[0] + 2.7,
                    "duration": 2.3,
                    "trial-type": "breath-out",
                }
                event_dataframe = event_dataframe.append(breathin, ignore_index=True)
                event_dataframe = event_dataframe.append(breathout, ignore_index=True)

            if row[7] == 5:
                hold = {"onset": row[0], "duration": 15, "trial-type": "hold"}
                event_dataframe = event_dataframe.append(hold, ignore_index=True)
            """
            #For the new version of the psychopy task
            if row[6] == 5:
                breathin = {"onset": row[0], "duration": 2.7, "trial-type": "breath-in"}
                event_dataframe = event_dataframe.append(breathin, ignore_index=True)
            if row[7] == 5:
                breathout = {"onset": row[0],"duration": 2.3,"trial-type": "breath-out"}
                event_dataframe = event_dataframe.append(breathout, ignore_index=True)
            if row[8] == 5:
                hold = {"onset": row[0], "duration": 2.7, "trial-type": "hold"}
                event_dataframe = event_dataframe.append(hold, ignore_index=True)
            """
        json_content = EVENTS_JSON_BOILERPLATE.copy()
        json_content["StimulusPresentation"]["Code"] = (
            "https://github.com/TheAxonLab/HCPh-fMRI-tasks/blob/"
            "97cc7879622f45129eefb9968890b41631f40851/task-bht_bold.psyexp"
        )
        json_content["trial_type"] = {}
        json_content["trial_type"][
            "Description"
        ] = "Indicator of type of action that is expected"
        json_content["trial_type"][
            "LongName"
        ] = "Breath-holding task conditions (that is, breath-in, breath-out, and hold)"
        json_content["trial_type"]["Levels"] = {
            "breath-in": "A green rectangle is displayed to indicate breathing in",
            "breath-out": """\
A yellow rectangle (orange for the last breath-in before hold) is \
displayed to indicate breathing out""",
            "hold": "A red rectangle is displayed to indicate breath hold",
        }

    elif "qct" in tsv_file:
        for index, row in df.iterrows():
            if int(row[0]) > 0:
                if row[6] == 5:
                    vis = {"onset": row[0], "duration": 3, "trial-type": "vis"}
                    event_dataframe = event_dataframe.append(vis, ignore_index=True)
                if row[7] == 5:
                    cog = {"onset": row[0], "duration": 0.5, "trial-type": "cog"}
                    event_dataframe = event_dataframe.append(cog, ignore_index=True)
                if row[8] == 5:

                    motor = {"onset": row[0], "duration": 5, "trial-type": "motor"}
                    event_dataframe = event_dataframe.append(motor, ignore_index=True)
                """
                #Will be used if an additional channel is added in AcqKnowledge
                if row[9] == 5:
                    blank = {"onset": row[0], "duration": 3, "trial-type": "blank"}
                    event_dataframe = event_dataframe.append(blank, ignore_index=True)
                """
        json_content = EVENTS_JSON_BOILERPLATE.copy()
        json_content["StimulusPresentation"]["Code"] = (
            "https://github.com/TheAxonLab/HCPh-fMRI-tasks/blob/"
            "97cc7879622f45129eefb9968890b41631f40851/task-qct_bold.psyexp"
        )
        json_content["trial_type"] = {}
        json_content["trial_type"][
            "Description"
        ] = "Indicator of type of action that is expected"
        json_content["trial_type"]["LongName"] = "Quality control task"
        json_content["trial_type"]["Levels"] = {
            "vis": "Fixation point on top of grating pattern",
            "cog": "Moving fixation points",
            "motor": """\
Finger taping with the left or right hand following the indications on the screen""",
            "blank": "Fixation point in the center of the screen",
        }
    elif "rest" in tsv_file:
        for index, row in df.iterrows():
            if row[4] == 5:
                movie = {"onset": row[0], "duration": 1200, "trial-type": "movie"}
                event_dataframe = event_dataframe.append(movie, ignore_index=True)
        """
        for index, row in df.iterrows():
            if row[6] == 5:
                fixation = {"onset": row[0], "duration": 3, "trial-type": "fixation point"}
                event_dataframe = event_dataframe.append(fixation, ignore_index=True)
            if row[7] == 5:
                fixation_end = {"onset": row[0], "duration": 0, "trial-type": "end fixation point"}
                event_dataframe = event_dataframe.append(fixation_end, ignore_index=True)
            if row[8] == 5:
                movie = {"onset": row[0], "duration": 1200, "trial-type": "movie"}
                event_dataframe = event_dataframe.append(movie, ignore_index=True)
            if row[9] == 5:
                movie_end = {"onset": row[0], "duration": 1200, "trial-type": "end movie"}
                event_dataframe = event_dataframe.append(movie_end, ignore_index=True)
        """
        json_content = EVENTS_JSON_BOILERPLATE.copy()
        json_content["StimulusPresentation"]["Code"] = (
            "https://github.com/TheAxonLab/HCPh-fMRI-tasks/blob/"
            "97cc7879622f45129eefb9968890b41631f40851/task-rest_bold.psyexp"
        )
        json_content["trial_type"] = {}
        json_content["trial_type"][
            "Description"
        ] = "Indicator of type of action that is expected"
        json_content["trial_type"]["LongName"] = "Resting state"
        json_content["trial_type"]["Levels"] = {
            "fixation point": "Fixation point in the center of the screen",
            "end fixation point": "End of fixation",
            "movie": "Movie",
            "end movie": "End of the movie",
        }
    output_folder = os.path.dirname(tsv_file)
    base_name = os.path.basename(tsv_file)
    # The from_channels might break the BIDS compatibility, but for now I don't know how else
    # to distinguish between events.tsv generated from the channels versus the psychopy log
    output_file = os.path.join(
        output_folder, base_name.replace("_physio.tsv.gz", "_from_channels_events.tsv")
    )
    event_dataframe.to_csv(output_file, sep="\t", index=False)
    print(f"Event DataFrame saved to {output_file}")

    json_file = os.path.splitext(output_file)[0] + ".json"
    with open(json_file, "w") as json_output:
        json.dump(json_content, json_output, indent=4)
    print(f"JSON metadata saved to {json_file}")

    plot_physio_data_with_events(df, event_dataframe, tsv_file)


def write_event_file_from_log(log: str) -> None:
    """
    Create a BIDS events file from the psychopy log.

    Parameters
    ----------
    log :obj:`os.pathlike`
         The path to the log output from psychopy.

    """
    with open(log, "r") as f:
        file = f.read()

        # Initialize events dataframe
        event_dataframe = pd.DataFrame(
            columns=["onset", "duration", "trial-type", "value"]
        )

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
                    # Store the start timestamp for "autoDraw=True"
                    start_timestamp[keyword] = timestamp

                elif status == "False" and keyword in start_timestamp:

                    # Calculate the duration for "autoDraw=False" if there is a corresponding "autoDraw=True"
                    onset = float(start_timestamp[keyword])
                    end = float(timestamp)
                    duration = end - onset

                    # Match keyword with associated sub-task
                    trial_type = TRIAL_TYPE[keyword]

                    # For the fingertapping and the eye movement sub-tasks, we have to encode which hand or the position
                    # of the fixation point to fully characterize the sub-task instance.
                    value = ""
                    if trial_type == "mot":
                        # Which hand is instructed to fingertap is encoded in the psychopy log one line above
                        # the onset 'ft_hand : autoDraw = True' and as the same timestamp as the onset.
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

                        # Extract the seven lines before the match
                        previous_lines = file.split("\n")[line_nbr - 7 : line_nbr]
                        previous_lines_text = "\n".join(previous_lines)

                        # Find all the matches using the regular expression
                        fix_pos_pattern = r"([\d.]+)\s+EXP\s+New trial \(rep=\d+, index=\d+\): OrderedDict\(\[\(\'xpos\', (-?\d+\.\d+)\), \(\'ypos\', (-?\d+\.\d+)\)\]\)"
                        matches = re.findall(fix_pos_pattern, previous_lines_text)
                        #If the patterns is found several times, the last appearance is the one corresponding to the event
                        timestamp, xpos, ypos = matches[-1]
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
                    onset = "{:.1f}".format(round(onset, 1))
                    duration = "{:.1f}".format(round(duration, 1))

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
        else:
            raise PatternNotFoundError(autodraw_pattern, log)

        output_folder = os.path.dirname(log)
        base_name = os.path.basename(log)
        # The from_log might break the BIDS compatibility, but for now I don't know how else
        # to distinguish between events.tsv generated from the channels versus the psychopy log
        output_file = os.path.join(
            output_folder, base_name.replace(".log", "_from_log_events.tsv")
        )
        event_dataframe.to_csv(output_file, sep="\t", index=False)
        return event_dataframe


def test_event(event_dataframe):
    from physio_event_test import TestEvents

    # Create a test suite with the TestEventsTSV test case
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEvents)

    # Pass the event DataFrame as an argument when creating the test case instance
    suite.testcase = TestEvents(event_dataframe)

    # Run the tests
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)


def write_all_event_files(folder_path: str) -> None:
    """
    Write events files.

    Find all files in the given folder with names containing "_physio.tsv.gz",
    write the corresponding event files and save a plot of the physiological data.

    Parameters
    ----------
    folder_path : :obj:`os.pathlike`
        Path to the folder containing the files.

    """
    file_list = os.listdir(folder_path)

    physio_files = [filename for filename in file_list if "_physio.tsv.gz" in filename]

    for filename in physio_files:
        file_path = os.path.join(folder_path, filename)
        write_event_file_from_channels(file_path)

    physio_log = [filename for filename in file_list if ".log" in filename]

    for filename in physio_log:
        file_path = os.path.join(folder_path, filename)
        event_dataframe = write_event_file_from_log(file_path)
        #test_event(event_dataframe)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Write event files and create plots for physiological data."
    )
    parser.add_argument(
        "--path",
        type=str,
        default=".",
        help="Path to the folder containing the files (default: current folder)",
    )
    args = parser.parse_args()
    write_all_event_files(args.path)
