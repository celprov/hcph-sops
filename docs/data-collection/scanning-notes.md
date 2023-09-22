## Quick guide to the protocol settings and configuration

### Editing a sequence
- [ ] Double click on the sequence name.
- [ ] After editing the sequence, you MUST store the changes if you want them to be kept by clicking on the <span class="consolebutton red">Go</span> button:

    ![launch_sequence.jpg](../assets/images/launch_sequence.jpg)

### Setting sequences for automatic start
- [ ] You can set the worker icon on the left of the sequence by clicking on it if you want to pause before starting that sequence. If the worker is not present, the sequence will launch automatically.

    ![worker_icon.jpg](../assets/images/worker_icon.jpg)

- [ ] Blocks with a name between double underscores `__*__` introduce an *Exam Paused* break.
    Such breaks prompt a modal dialog with the *Exam Paused* title like this:

    ![exam_paused.jpg](../assets/images/exam_paused.jpg)

    !!! warning "The *Patient has Contrast Agent* checkbox MUST always be unchecked, as this protocol does not involve a contrast agent""

- [ ] Click <span class="consolebutton red">Continue</span> when you are ready to proceed.

### Setting the FoV
!!! warning "Using the anatomical image to adjust the field-of-view (FoV) is RECOMMENDED"

    - [ ] Drag and drop the protocol's stack icon (🗇) corresponding to the `anat-T1w__mprage` sequence into the image viewer.
        The icon will appear AFTER the image has been acquired.

- [ ] Make sure that the FOV (yellow square) includes the whole brain by tilting or translating the FOV. If the full brain, including the cerebellum, do not fit in the FOV, favorise making sure that the cortex is fully enclosed in the yellow square. For reproducibility, it is better if the FOV across sequences have a similar center and a similar tilt. However, if it is not possible, the priority remains to include the whole brain in the FOV.
- [ ] If two sequences have the same resolution and the same number of slices, you can copy paste the FOV
    - [ ] Open the sequence for which you want to adjust the FOV/geometry
    - [ ] Right click on the sequence for which the FOV has already been carefully positioned
    - [ ] Select `Copy Parameters`
    - [ ] `Center of slice groups and saturation regions`
- [ ] Once the FOV is well placed, store the new settings of the sequence by pressing <span class="consolebutton red">Go</span>.

    ![adjustFOV.jpg](../assets/images/adjustFOV.jpg)

## Eye-Tracker Calibration Process

- [ ] On the eye-tracking (ET) computer, ensure that the appropriate calibration type is selected (9-point for QCT and 5-point for resting state and breath-holding tasks):
    - [ ] Click on <span class="keypress">Set Options</span> located on the right side of ET computer screen.
    - [ ] Under **Calibration type** in the top left corner, choose the image containing either 9 or 5 points.

        ![9-points_calibration](../assets/images/9-points_calibration.jpg)

- [ ] Two crosses should appear on the ET computer screen: one at the center of the pupil and the other at the center of the corneal reflection.

    !!! warning "If the two crosses do not appear, the coverage, focus and intensity of the ET are incorrect"

        - [ ] Repeat the steps for their setting up given in [the participant's preparation section](participant-prep.md#final-preparatory-steps-of-the-et)

- [ ] Initiate the ET calibration by pressing <span class="keypress">C</span> on the laptop keyboard or by clicking on <span class="keypress">Calibration</span> on the ET interface.
- [ ] Once the participant's gaze stabilizes on the first fixation point, the <span class="keypress">Accept Fixation</span> button turns green.
    Click on it to confirm the initial position.

    ![accept_fixation](../assets/images/accept_fixation.jpg)

- [ ] Subsequent positions should be automatically validated when the gaze remains stable.
    If not, manually click the <span class="keypress">Accept Fixation</span> button when it turns green.
- [ ] After the calibration, ensure that the fixation points' positions match the expected pattern corresponding to the 9- or 5-point calibration.
    If the pattern appears too distorted, restart the calibration.
- [ ] Upon successful calibration, initiate validation by clicking <span class="keypress">Validation</span> on the ET interface or pressing the <span class="keypress">V</span> key on the laptop keyboard. Follow the same instructions as in the calibration to validate positions.
- [ ] If validation fails, repeat previous steps and restart calibration. Otherwise, you can leave the calibration mode and proceed with the task program by pressing the <span class="keypress">Esc</span> key on the laptop (*{{ secrets.hosts.psychopy | default("███") }}*).

## Scanner interface
The picture below shows you the scanner interface as you will see it when you operate the MR machine. The arrow points to the screen and the red circles indicate the control buttons.
![alarm_button](../assets/images/alarm_button.png)


### Scanner's settings buttons

Adjust settings by pressing the respective button and then turning the central knob (1) to adjust the setting to the desired level:

![ventilation_button](../assets/images/ventilation_button.png)

- [ ] Use the headphones :fontawesome-solid-headphones: button (2) to adjust the volume of the earphones.
- [ ] Use the speaker :fontawesome-solid-volume-off: button (3) to adjust the volume of the air speaker in the scanning room.
- [ ] Use the light :fontawesome-solid-lightbulb: button (4) to adjust the intensity of the illumination inside the scanning room.
- [ ] Use the fan :fontawesome-solid-fan: button (5) to adjust the ventilation in the scanning room.

!!! warning "The central knob (button 1) will turn off the alarm if pushed when the alarm is on"

### Standard extraction of the participant

There are two options to extract the participant, when the session has concluded or within the session if the participant needs to be extracted and there is no emergency (e.g., in case of technical error the scanner does not permit continuing the session and it needs to be aborted).

| ![take_table_down](../assets/images/take_table_down.png) | ![quick_return](../assets/images/quick_return.png) |
|:--:|:--:|
| *The participant can be extracted by pressing the extraction button (bottom arrow in the leftmost picture) and then genly rolling the central knob. Alternatively, you can just press the* Home :fontawesome-solid-house: *button (rightmost picture).* {: colspan=2} |
