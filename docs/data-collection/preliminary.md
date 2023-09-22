## Once, at the beginning of the project

### Setting up the scanner protocol at the MR console

The pilot phase will conclude when the protocol is decided upon.
Once finalized the protocol design, it will be *frozen* and it cannot be changed anymore.

- [ ] (Optional) Load an existing protocol
- [ ] Edit the protocol as needed

    !!! important "Follow Reproin conventions"

        When assigning names to the MR sequences in the protocol, make sure to follow the [Reproin conventions](https://dbic-handbook.readthedocs.io/en/latest/mri/reproin.html) to maximally facilitate the conversion into BIDS.

- [ ] Update the *Number of measurements* in all `func-bold_task-*` sequences, according to the [previously recorded timings](intro.md#task-timing):

    $$N_\text{measurements} = L_t / \text{TR}, \quad t \in \{\text{bht}, \text{qct}, \text{rest}\},$$

    where $L_t$ is the length of a particular task $t$ (either BHT, QCT, or resting state) in seconds as timed before, and
    $\text{TR}$ is the **repetition time** of the BOLD sequence, in seconds.

- [ ] Save the protocol

    !!! warning "Logging in as an advanced user is required before saving the protocol"

        As a good practice, always work as the standard user `{{ secrets.login.username_scanner | default("janedoe") }}`.
        However, you MUST change into *advanced user mode* before saving the protocol.

        Simultaneously press the <span class="keypress">Tab</span> + <span class="keypress">Delete</span> + <span class="keypress">:octicons-sign-out-16:</span> on the control-computer's keyboard:

        > Username: `{{ secrets.login.superusername_scanner | default("superjanedoe") }}`
        >
        > Password: `{{ secrets.login.superuserpass_scanner | default("******") }}`

        !!! danger "After three wrong password entries, access will be denied, and only a Siemens engineer will be able to unlock the MR scanner."

    - [ ] Open the Dot-Cockpit window
        ![](../assets/images/save_protocol1.jpg)
    - [ ] In `Browse`, find the right folder to save the protocol in (*RESEARCH* ⤷ *Oscar*).
    - [ ] Right click on the folder and select *New* ⤷ *Program*. This opens an empty page in the program editor
        ![](../assets/images/save_protocol2.jpg)
        ![](../assets/images/save_protocol3.jpg)
    - [ ] Select all the sequences you want to run from the sequence list and click right to copy.
        ![](../assets/images/save_protocol4.jpg)
    - [ ] Drag or paste the copied sequences in the program editor.
        ![](../assets/images/save_protocol5.jpg)
    - [ ] Once finished, click on the floppy disk icon (:fontawesome-solid-floppy-disk:) in the upper left to save.
    - [ ] Give the protocol a relevant name starting with the date of acquisition in the format YYYYMMDD and click <span class="consolebutton">Save</span>.
        ![](../assets/images/save_protocol6.jpg)
    - [ ] If desired, the protocol details can also be downloaded as a pdf on a peripherical USB key.
        - [ ] Right-click on the protocol and select *Print*
        - [ ] Save the PDF in your USB key.
- [ ] Make sure you save a different protocol for each of the four PE directions (i.e., AP, PA, LR, RL).

### Install the BIOPAC

- [ ] Make sure you understand the components and settings of the BIOPAC, described above.
- [ ] Set up the line frequency switches on the back of the BIOPAC amplifier depending on your country frequency to reduce noise. Both switches should be DOWN if your country's line frequency is 50Hz. Both switches should be UP if your country's line frequency line is 60Hz.
    ![biopack-frequency-switch](../assets/images/biopack-frequency-switch.jpg "BIOPAC frequency switch")
- [ ] Plug the different units of the BIOPAC together if it has not been done yet.
- [ ] Ensure that the *Mode* switch of the [MMBT-S Trigger Interface Box adapter (pink color box)](../assets/files/MMBT-S_instruction_manual_v2.2.pdf) is set on the **P** position.
- [ ] Install the BIOPAC recording software (*AcqKnowledge*).
- [ ] Create a template *graph file* ([`EXP_BASE.gtl`](../assets/files/EXP_BASE.gtl))

    !!! important "Creating the *AcqKnowledge*'s template graph file"

        - [ ] Creating a graph file requires the BIOPAC system powered up and connected to the *{{ secrets.hosts.acqknowledge | default("███") }}* computer.
        - [ ] Add the RB module
            - [ ] Check the channel on top switch of the unit: the <mark>DA100C</mark> MUST be set on **channel 1**.
            - [ ] Under the tab *Analog*, click on *Add new module*.
            - [ ] Find the name of the BIOPAC unit corresponding to the <mark>DA100C</mark>.
            - [ ] Set the module settings (gain, filters, etc.) corresponding to those of the configuration switches in the front of the module.
            - [ ] When prompted to enter the calibration points, map the interval [-5, 0] to [0, 10]. You invert the sign of the interval for the interpretation to be more clear.
        - [ ] Add the ECG module
            - [ ] Check the channel on top switch of the unit: the <mark>ECG100C MRI</mark> MUST be set on **channel 2**.
            - [ ] Under the tab *Analog*, click on *Add new module*.
            - [ ] Find the name of the BIOPAC unit corresponding to the <mark>ECG100C</mark>.
            - [ ] Set the module settings (gain, filters, etc.) corresponding to those of the configuration switches in the front of the module.
            - [ ] When prompted to enter [calibration?], for the ECG you should map the interval ?? to ??.
        - [ ] Add the GA module
            - [ ] Confirm that the CO<sub>2</sub> output of the GA is connected through the ANISO filter to the **channel 3** of the AMI100C module.
            - [ ] Under the tab *Analog*, click on *Add new module*.
            - [ ] Select *Custom* and then indicate it is connected to **channel 3** by selecting *AMI/HLT - in3*.
            - [ ] When prompted to enter the calibration points, map the interval [0.03, 1.0] to [0, 10.0].
        - [ ] Add the Digital inputs
            - [ ] Under the tab *Digital*, click on *Add new module*.
            - [ ] The parallel cable feeds into ports <mark>D8-D15</mark>.
        - [ ] Configure the sampling frequency
        - [ ] Configure the experiment length (at least 2.5 hours)
        - [ ] Configure whether you want to collect directly to hard disk and autosave settings
        - [ ] Save the experiment, making sure you choose a "graph template file" (with extension `.gtl`)

### Install the gas analyzer (GA)



### Preparing the *Stimuli presentation laptop* ({{ secrets.hosts.psychopy | default("███") }})

This block describes how to prepare a laptop with a running *Psychopy 3* installation, the *EyeLink* software corresponding to the Eye Tracker, and finally an *Experiment synchronization service*.

#### Stimuli presentation with *psychopy*

- [ ] [Fork the HCPh-fMRI-tasks repository](https://github.com/TheAxonLab/HCPh-fMRI-tasks/fork) under your user on GitHub.
- [ ] Clone the [HCPh-fMRI-tasks repository](https://github.com/TheAxonLab/HCPh-fMRI-tasks):
    ```
    git clone git@github.com:<your-gh-username>/HCPh-fMRI-tasks.git
    ```
- [ ] Set-up the original repository as upstream remote:
    ```
    git remote add upstream git@github.com:theaxonlab/HCPh-fMRI-tasks.git
    ```
- [ ] Log on *{{ secrets.hosts.psychopy | default("███") }}* with the username *{{ secrets.login.username_psychopy| default("███") }}* and password `{{ secrets.login.password_psychopy| default("*****") }}`.

- [ ] Clone the [PsychoPy repository](https://github.com/psychopy/psychopy.git):
    ```
    git clone git@github.com:psychopy/psychopy.git
    ```
- [ ] Navigate to the Psychopy directory:
    ```
    cd psychopy
    ```
- [ ] Psychopy should not be installed with anaconda. If an anaconda environment is activated, run the following command to deactivate it:
    ```
    conda deactivate
    ```
- [ ] Update pip to the latest version:
    ```
    pip3 install --upgrade pip
    ```
- [ ] Install bdist_mpkg, py2app and attrdict:
    ```
    pip3 attrdict py2app bdist_mpkg
    ```
- [ ] Install Psychopy using the following command:
    ```
    pip3 install -e .
    ```
- [ ] Open Psychopy, open the experiment-files corresponding to each task:
    - [ ] {{ settings.psychopy.tasks.func_qct }} (positive-control task, QCT) :
        - [ ] time it to confirm the length, and
        - [ ] check the task runs properly.
    - [ ] {{ settings.psychopy.tasks.func_rest }} (resting-state fMRI):
        - [ ] time it to confirm the length, and
        - [ ] check that the movie is played.
    - [ ] {{ settings.psychopy.tasks.func_bht }} (breath-holding task, BHT):
        - [ ] time it to confirm the length, and
        - [ ] check the task runs properly.

#### Installing *EyeLink* (eye tracker software)

- [ ] Log on *{{ secrets.hosts.psychopy | default("███") }}* with the username *{{ secrets.login.username_psychopy | default("███") }}* and password `{{ secrets.login.password_psychopy | default("*****") }}`.

- [ ] Enable Canonical's universe repository with the following command:
    ```
    sudo add-apt-repository universe
    sudo apt update
    ```
- [ ] Install and update the ca-certificates package:
    ```
    sudo apt update
    sudo apt install ca-certificates
    ```
- [ ] Add the SR Research Software Repository signing key:
    ```
    sudo apt-key adv --fetch-keys https://apt.sr-research.com/SRResearch_key
    ```
- [ ] Install the EyeLink Developers Kit:
    ```
    sudo apt install eyelink-display-software
    ```
- [ ] Install the EyeLink Data Viewer:
    ```
    sudo apt install eyelink-dataviewer
    ```

#### Setting up a synchronization service

!!! important "It's fundamental to have a reliable means of communication with the BIOPAC digital inputs"

    The following guidelines set up a little service on a linux box that keeps listening for key presses (mainly, the <span class="keypress">s</span> trigger from the trigger box), and RPC (remote procedure calls) from typically *Psychopy* or similar software.

    The service is spun up automatically when you connect the MMBT-S modem interface that communicates with the BIOPAC (that is, the *N-shaped pink box*)

- [ ] Copy the [latest version of the code to send triggers](https://github.com/TheAxonLab/hcph-sops/blob/mkdocs/code/synchronization/forward-trigger-service.py)
- [ ] To automatically start the program when the BIOPAC is connected, create a udev rule as follows:
    ```
    sudo nano /etc/udev/rules.d/99-forward-trigger.rules
    ```
- [ ] Add the following rule to the file:
    ```
    ACTION=="add", KERNEL=="ttyACM0", SUBSYSTEM=="tty", TAG+="systemd", ENV{SYSTEMD_WANTS}="forward-trigger.service"
    ```
- [ ] Save the file and exit the editor.
- [ ] Run the following command to reload the udev rules:
    ```
    sudo udevadm control --reload-rules
    ```
- [ ] Create a systemd service unit file:
    ```
    sudo nano /etc/systemd/system/forward-trigger.service
    ```
- [ ] Add the following content to the file (Adapt the path to forward-trigger.py to the location on your computer):
    ```
    [Unit]
    Description=Forward Trigger Service
    After=network.target

    [Service]
    ExecStart=/usr/bin/python3 /path/to/forward-trigger.py
    WorkingDirectory=/path/to/forward-trigger/directory
    StandardOutput=null

    [Install]
    WantedBy=multi-user.target
    ```
- [ ] Save the file and exit the text editor.
- [ ] Run the following command to enable the service to start at boot:
    ```
    sudo systemctl enable forward-trigger
    ```
- [ ] Run the following command to reload the systemd daemon:
    ```
    sudo systemctl daemon-reload
    ```

??? important "Testing the service without the syncbox connected"

      - [ ] Ensure `socat` and `screen` are installed (if not already):
          ```
          sudo apt-get update
          sudo apt-get install socat screen
          ```
      - [ ] Create a virtual serial port and establish a symbolic link to `/dev/ttyACM0` using the following command:
          ```
          sudo socat PTY,link=/tmp/virtual_serial_port PTY,link=/dev/ttyACM0,group-late=dialout,mode=666,b9600
          ```
      - [ ] With `screen`, listen to the new virtual serial port:
          ```
          screen /dev/ttyACM0
          ```
      - [ ] Press <span class="keypress">s</span> and verify that `^A` appears in the screen terminal.

## Every two months

### Calibrate the GA

??? important "A gas mixture bottle with a known CO<sub>2</sub> and O<sub>2</sub> concentrations is necessary"

    CO<sub>2</sub> concentration must be between 5% and 10%, while O<sub>2</sub> within 5% and 21%.
    A second reference mixture is necessary, and room air can be used, knowing that atmospheric contents by volume are 0.039 ±0.001%
    for CO<sub>2</sub> and 20.946 ±0.003% for O<sub>2</sub>.

- [ ] Connect the GA to the BIOPAC as described above.
- [ ] Connect the BIOPAC to the *Physiology recording laptop* ({{ secrets.hosts.acqknowledge | default("███") }}) as described above.
- [ ] Connect the *AcqKnowledge* License Key into a USB Port of the *Physiology recording laptop* ({{ secrets.hosts.acqknowledge | default("███") }}).
- [ ] Open *AcqKnowledge* software on the *Physiology recording laptop* ({{ secrets.hosts.acqknowledge | default("███") }}).
- [ ] Open the template *graph file* ([`EXP_BASE.gtl`](../assets/files/EXP_BASE.gtl))
- [ ] Edit the configuration of the inputs 3 (connected to the CO<sub>2</sub> output of the GA) and 4 (connected to the O<sub>2</sub> output of the GA).
    Lower and upper calibration points can be set by sampling the input a number of times with the *AcqKnowledge* utility.
- [ ] Overwrite the template *graph file* `EXP_BASE.gtl`.
