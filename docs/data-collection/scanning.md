
!!!danger "Familiarize with emergency procedures"
    You MUST know the security procedures in case of problem and keep yourself updated with changes.
    Some of the emergency procedures are found [here](emergency-procedures.md).

    In addition to the brief guidelines given in these SOPs, further safety information is found in {{ secrets.tribu.mri_security | default("███") }}.


## During the session

- [ ] Check in with the participant frequently, not necessarily only at the scripted points.
- [ ] Watch for motion and arousal state using the ET's camera.
      If you detect motion or the participant falls asleep at inadequate points, use the speaker to inform them.

## Check experimental setup
!!! danger "DO NOT FORGET to check the readiness of the experimental setup at this point"

- [ ] Check the trigger box:
    - [ ] the box is on,
    - [ ] *Synchronization mode* is on,
    - [ ] session has been started,
    - [ ] USB cable to *{{ secrets.hosts.psychopy | default("███") }}* is connected.
- [ ] Check the GA:
    - [ ] the tubing coming from the scanning room is properly connected,
    - [ ] the CO<sub>2</sub> BNC output is plugged through the filter to the BIOPAC AMI200, on input channel 3,
    - [ ] **the exhaust cap IS REMOVED**
    - [ ] the GA is on (switch it on if necessary),
    - [ ] ensure **the PUMP IS ON**, and
    - [ ] **turn the pump's power knob to MAXIMUM position**.
- [ ] Check *{{ secrets.hosts.psychopy | default("███") }}*:
    - [ ] has enough battery, and plug the power cord if necessary;
    - [ ] USB cable to the MMBT-S Trigger Interface Box is connected;
    - [ ] serial cable from the MMBT-S Trigger Interface Box is connected to the back of the SPT100D digital interface (gray block) of the BIOPAC;
    - [ ] computer is ready, with psychopy open, and with the appropriate version of experiments; and
    - [ ] leave the computer with a pleasant screen projecting (e.g., a gray background).
- [ ] Check *{{ secrets.hosts.acqknowledge | default("███") }}*:
    - [ ] has enough battery, and plug the power cord if necessary;
    - [ ] computer is ready, with the *AcqKnowledge* software open and collecting data;
    - [ ] check the ECG and RB signals, and fix unanticipated problems (e.g., the respiration belt needs to be fastened tighter);
    - [ ] the *Amphetamine* app is running and keeping the computer unlocked while *AcqKnoledge* is working.

## Acquire a localizer (*AAhead_scout*)
- [ ] Indicate the participant that the scanning will soon start:

    ???+ quote "Tell the participant that we are starting"
        Hey [NAME], we are about to start our first scan run.

        This is going to be a long session, so please make sure you are feeling as comfortable as you possibly can in there.
        Remember not to cross your legs or hold your hands together and check your back is also comfortable.
        I'm going to ask you to take a deep breath now, so I can check the respiration belt is properly set up.
        If it is too tight, please let me know.

        [Allow a few moments for the participant to breathe while you check the recordings]

        Okay, we seem to be able to track your respiration. Is the respiration belt too restraining?
        This is also a good moment to swallow, and to check your neck and head are in a comfortable position.

        For this first part, all you have to do is stay still; you can relax and close your eyes if it helps.

        Are you ready?

- [ ] Wait for the participant confirmation and set the speaker off afterward.
- [ ] Launch the `AAhead_scout_{32,64}ch-head-coil` protocol by pressing *Continue* :fontawesome-solid-play:{ .redcolor }.
- [ ] Once the localizer is concluded, you can drag and drop the image stack icon (something like 🗇, with an object on the top stack) onto the image viewer. That will open the localizer on the viewer.

    ![drag_t1w.jpg](../assets/images/drag_t1w.jpg)

### If the localizer presents very low quality

!!! warning "The localizer may present very low quality if the head-coil has not been properly initiated by the scanner"

- [ ] Enter the scanning room, extract the participant from the scanner by pressing the home (:fontawesome-solid-house:) button.
- [ ] Tell the participant that you need to reset the head coil
- [ ] Unplug and replug the head coil
- [ ] Check that the coil has been properly detected in the scanner's monitor
- [ ] Re-insert the participant in the scanner
- [ ] Re-run the `AAhead_scout_{32,64}ch-head-coil` protocol.

## Acquire a high-resolution, anatomical image

- [ ] Launch the `anat-T1w__mprage` protocol by pressing *Continue* :fontawesome-solid-play:{ .redcolor }.

    !!! warning "While you are still running the MPRAGE sequence"
        - [ ] Open the parameters of the sequence named `fmap-phasediff__gre` and ensure that under *Contrast* ⤷ *Reconstruction* the option *Magnitude et phase* is selected. This is crucial so that both the magnitude and the phase difference field map images are saved.
        - [ ] Repeat the configuration of *Magnitude et phase* for all sequences name `fmap-epi_acq-bold_dir-{RL,LR,PA,AP}__*`.
        - [ ] Repeat the configuration of *Magnitude et phase* for all sequences name `func-bold_task-{bht,qct,rest}_dir-{RL,LR,PA,AP}__cmrr_me4_sms4`.
        - [ ] Open the `dwi-dwi_dir-{RL,LR,PA,AP}__279dir_monopolar` sequence and under the section *Diff.*, uncheck all the derivatives except for *Diff. Weighted Image*.

## Acquire the diffusion MRI run

- [ ] [Adjust the FoV](scanning-notes.md#setting-the-fov) of the `dwi-dwi_dir-{RL,LR,PA,AP}__279dir_monopolar` sequence as indicated below.
- [ ] Verify again the `dwi-dwi_dir-{RL,LR,PA,AP}__279dir_monopolar` parameters under section *Diff.* All the derivatives MUST be unchecked except for *Diff. Weighted Image*.
- [ ] Inform the participant that the diffusion scan will follow.

    ??? quote "Only for the participant of Cohort I"

        Hey Oscar, we are ready to proceed with the diffusion scan.
        The BIOPAC is functional and *AcqKnowledge* is properly registering the respiration belt and ECG.
        The gas analyzer is ON, but it is still warming up.
        The psychopy computer is ready.
        Are you ready?

    ???+ quote "Participant of Cohort II"

        Hey [NAME], the next block is a bit long, around 30 minutes.

        You can close your eyes and even sleep if you wish.

        I'm going to give you a short time (ten seconds or so) to swallow, and perhaps accommodate your back or your arms. However, please try not to move your head.

        It is critical that you don't move, especially at all at the very beginning and the next 20 seconds after you hear the first blipping sounds.

        Try to minimize swallowing, and eye movements (for example, blinking) and try to maintain comfortable and shallow breathing.

        Are you ready?

- [ ] Launch the diffusion `dwi-dwi_dir-{RL,LR,PA,AP}__279dir_monopolar` sequence by pressing *Continue* :fontawesome-solid-play:{ .redcolor }.
- [ ] While it is running, [adjust the FoV](scanning-notes.md#setting-the-fov) for the following sequence.

!!! important "At this point, the GA should have finished the warm-up so you can verify it is working"

    - [ ] Ask the participant to take three deep breathes, to then go back to a comfortable, normal respiration pace. Check on the *AcqKnoledge* window that the three breathes are distinctly registered (taking into account that there may be 10-25 seconds of delay because of the tubing).

### Once the main diffusion MRI run is done, proceed with fieldmaps
- [ ] Launch the DWI-EPI sequence `fmap-epi_acq-b0_dir-{RL,LR,PA,AP}__6dir_monopolar` for *B<sub>0</sub>* field mapping by pressing *Continue* :fontawesome-solid-play:{ .redcolor }.
- [ ] While it is running, [adjust the FoV](scanning-notes.md#setting-the-fov) for the following sequence.
- [ ] Launch the GRE (*phase difference*) sequence `fmap-phasediff__gre` for *B<sub>0</sub>* field mapping by pressing *Continue* :fontawesome-solid-play:{ .redcolor }.
- [ ] While it is running,
    - [ ] [Adjust the FoV](scanning-notes.md#setting-the-fov) for the following sequence.
    - [ ] Verify that in the next sequence parameters under *Contrast>Reconstruction* the option *Magnitude et phase* is selected!
- [ ] Launch the BOLD-EPI sequence `fmap-epi_acq-bold_dir-{RL,LR,PA,AP}__cmrr_me4_sms4` for *B<sub>0</sub>* field mapping by pressing *Continue* :fontawesome-solid-play:{ .redcolor }.
- [ ] While the fieldmap sequence is running,
    - [ ] [Adjust the FoV](scanning-notes.md#setting-the-fov) for the positive-control-task (`func-bold_task-qct_dir-{RL,LR,PA,AP}__cmrr_me4_sms4`) fMRI sequence following the abovementioned steps, and
    - [ ] verify the *Number of measurements* with respect to the [task's timing](intro.md#task-timing) ({{ settings.mri.timings.func_qct }}).
    - [ ] Verify that the positive-control task {{ settings.psychopy.tasks.func_qct }} is open in psychopy, that you calibrated the ET.

## Acquire the functional MRI block
- [ ] Inform the participant about the fMRI block

    ???+ quote "Starting the fMRI block - calibrating the eye tracker"
        Hey [NAME], we are now to move into measuring the activity of your brain.

        Is everything alright thus far?

        [Allow some time for response]

        Before we start, we need to calibrate the eye-tracker device, which follows your right eye during experiments.

        Your are going to see a round fixation point, and the point is going to move randomly over the screen space.
        Please follow it with your gaze, trying to look at it as stable as possible and without moving your head.

        Are you ready?

- [ ] Wait for confirmation, respond to follow-up comments, and [initiate the ET calibration (instructions below)](scanning-notes.md#eye-tracker-calibration)

### Quality-control task (QCT)
- [ ] Verify that the task's program is awaiting the scanner's trigger to start.
- [ ] Inform the participant that we will proceed with the quality-control task (QCT). Repeat task instructions.

    ???+ quote "Starting the positive control task"
        Hey [NAME], thanks for your collaboration with the eye tracking calibration.

        The following block will collect some behavioral data and requires your collaboration.
        You will be exposed to several activities.

        Whenever you see a red circle, please fix your gaze on it, wherever it is shown on the screen.
        If the red circle moves, we ask you to follow it with your eyes.

        Some other times, you'll see either "RIGHT" or "LEFT" written on the screen. During those times, please tap your thumb and the other fingers of your right or left hand as indicated on the screen.

        Before we start, please leave the alarm button on your tummy to free your hand for finger tapping. Please do not hesitate to grab it in case you need to squeeze it.

- [ ] Launch the `func-bold_task-qct_dir-{RL,LR,PA,AP}__cmrr_me4_sms4` protocol by pressing *Continue* :fontawesome-solid-play:{ .redcolor }.
- [ ] Wait for the calibration scans to be finished (the process is reported on the bottom left corner of the console) and verify that the first volume's trigger signal was received by *{{ secrets.hosts.psychopy | default("███") }}* (meaning **CHECK that the task program was initiated**).
- [ ] While it is running:
    - [ ] [Adjust the FoV](scanning-notes.md#setting-the-fov) for the following sequence,
    - [ ] verify the *Number of measurements* with respect to the [task's timing](intro.md#task-timing) ({{ settings.mri.timings.func_rest }}), and
    - [ ] double check that it has the setting *Magnitude et phase* selected in the drop-down menu under *Contrast>Reconstruction*.
- [ ] Once the sequence is over, close the current experiment on psychopy and open {{ settings.psychopy.tasks.func_rest }}.

### Resting state fMRI
- [ ] Inform the participant:

    ???+ quote "Quick re-calibration the ET before continuing"
        Thanks [NAME], that was a short behavioral task.

        Before moving on, we will run another calibration of the eye tracker, please follow the moving fixation point.

        Is everything alright?

- [ ] Wait for confirmation, respond to follow-up comments, and [initiate the ET calibration (instructions below)](scanning-notes.md#eye-tracker-calibration)
- [ ] Once the ET is calibrated, verify that the task is left and awaiting for the sequence's trigger to start.
- [ ] Inform the participant that the next sequence is resting-state fMRI (rsfMRI).

    ???+ quote "Starting the resting-state block"
        Hey [NAME], we are about to start resting-state fMRI.

        For this scan, all you have to do is stay still, and look at the movie.
        Please do not close your eyes, and it is particularly critical that you don't move at all in the initial moments of the acquisition block.

        Are you ready?

- [ ] Launch the rsfMRI sequence `func-bold_task-rest_dir-{RL,LR,PA,AP}__cmrr_me4_sms4` by pressing *Continue* :fontawesome-solid-play:{ .redcolor }.
- [ ] While it is running:
    - [ ] [Adjust the FoV](scanning-notes.md#setting-the-fov) for the following sequence,
    - [ ] verify the *Number of measurements* with respect to the [task's timing](intro.md#task-timing) ({{ settings.mri.timings.func_bht }}), and
    - [ ] double check that it has the setting *Magnitude et phase* selected in the drop-down menu under *Contrast>Reconstruction*.
- [ ] Once the sequence is over, close the current experiment on psychopy and open {{ settings.psychopy.tasks.func_bht }}.

### Breath-holding task (BHT)
- [ ] Inform the participant:

    ??? quote "Quick re-calibration the ET before continuing"
        Thanks [NAME], that was a long behavioral block.

        Before moving on, we will run another calibration of the eye tracker, please follow the moving fixation point.

        Is everything alright?

- [ ] Wait for confirmation, respond to follow-up comments, and [initiate the ET calibration (instructions below)](scanning-notes.md#eye-tracker-calibration)
- [ ] Once the ET is calibrated, verify that the task is left and awaiting for the sequence's trigger to start.
- [ ] Inform the participant that the next sequence is breath-holding task fMRI. Repeat the instructions for the task.

    ???+ quote "Starting the breath-holding task"
        Hey [NAME], we will proceed now with a breath-holding task.

        I remind you that you have to breathe following the cues of the colored rectangle.

        Green means "BREATHE IN", orange means "BREATHE OUT" and red means "HOLD YOUR BREATH".

        Remember to not follow the breathing instructions during the first block and to exhale the small amount of air you have remaining at the end of the hold.

        Are you ready?

- [ ] Launch the `func-bold_task-bht_dir-{RL,LR,PA,AP}__cmrr_me4_sms4` sequence by pressing *Continue* :fontawesome-solid-play:{ .redcolor }.
- [ ] While it is running, determine whether there is enough time to run the anatomical T2-weighted run. If so, [adjust the FoV](scanning-notes.md#setting-the-fov) for the following sequence.


!!! warning "ONLY if time permits"

    - [ ] Launch the `anat-T2w__flair` protocol by pressing *Continue* :fontawesome-solid-play:{ .redcolor }

## Concluding the session

- [ ] Inform the participant:

    ???+ quote "Session is finished"
        Thanks [NAME], the session has concluded and we will shortly let you out of the scanner.

!!! warning "These operations may be done during the T2w acquisition"

    - [ ] Stop the *AcqKnowledge* recording on the *{{ secrets.hosts.acqknowledge | default("███") }}* computer.
    - [ ] Switch the BIOPAC MP160 module off.
    - [ ] Turn off the pump of the GA.
    - [ ] Switch the GA off.
    - [ ] Put the exhaust and inlet caps back.

- [ ] The exam is over, you can proceed with the [tear-down protocol](./tear-down.md).
