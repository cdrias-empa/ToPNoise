# 9. Troubleshooting

**Checklist for this chapter**

- [ ] I know where each module writes its messages (section 9.1).
- [ ] I have read the last lines of the terminal window of the module before looking for a solution.
- [ ] Before I ask for help, I have collected the information of section 9.7.

## 9.1 Where to look first

When something does not work, the answer is almost always written somewhere. Look there first.

| What failed | Where the message is |
|---|---|
| The launcher | The terminal in which you typed `bash run.sh` |
| A module does not open, or stops | The **terminal window (xterm) that opened with the module**. It stays open on purpose (chapter 3). Read its last lines |
| An input is wrong | A **message window** of the module, with the text of the error |
| Multi-Sleeper Model calculation | The terminal windows of the jobs (keep them open with *Debug mode*; close them by hand afterwards, the calculation continues only then), the folder `Messages` and the file `Outputs/log.txt` of the calculation (chapter 4) |
| Wheelset FE calculation | `<simulation>/<position>/vertical/Messages/message_Stage2.mess`. When a calculation fails, the folders `Phase1_Modes` and `Phase2_FRF` are kept (chapter 5) |
| Boundary Element calculation | The *Progress* area, and the files `log.txt` and `error_message.txt` in the result folder of the row (chapter 6) |
| Post-processing calculation | A message window, and the terminal window of the module (chapter 7) |

In the Code_Aster message files (`.mess`), the errors are the lines that start with `<F>` (fatal) or `<S>`.

## 9.2 Installation and launch

Each line gives what you see, why, and what to do.

| What you see | Why | What to do |
|---|---|---|
| `singularity: command not found` | Singularity is not installed, or not in your path | Go back to section 2.2 |
| After `bash run.sh`, no window opens, and the terminal says `qt.qpa.xcb: could not connect to display` | Your terminal has no access to a display | Use a terminal opened from the desktop (section 1.4), or the [remote access appendix](appendix-remote.md) |
| A button of the launcher does nothing, and the terminal of `bash run.sh` says `sh: 1: xterm: not found` | `xterm` is not installed | Install it: `sudo apt install xterm` |
| The terminal window of a module shows `FATAL: could not open image …: no such file or directory` | The image is not in the `images` folder, or it has another name | Check with `ls images` that the four files of section 2.3 are there, with these names |
| `FATAL: could not open image …: SIF image … is corrupted: wrong partition size` | The image is incomplete. The download was interrupted, or the file was not fully copied | Delete the file and download it again. For the Boundary Element image, join the two parts again (section 2.3) |
| `FATAL: could not open image …: image format not recognized` | The file is not an image. It can be an error page saved under the name of the image, or the two parts of the Boundary Element image that were not joined | Download the image again. Check its size with `ls -l images` (section 2.4) |

<!--
Messages that are due to known problems of version 1.0.0-beta. Remove each one when its fix is released.
- "E: Package 'singularity-container' has no installation candidate" while installing Singularity on Ubuntu 22.04 or earlier (fix pending G4: the package exists only on Ubuntu 24.04 and later).
- "ERROR 404: Not Found" from `bash setup/download_images.sh` (fix pending G5: no release is published).
- "FATAL: container creation failed: mount /mnt/results->/mnt/results error: while mounting /mnt/results: mount source /mnt/results doesn't exist" when a module is started (fix pending G1).
- "TopNoise root directory was not provided by the launcher." when the Boundary Element module is started (fix pending G2).
- "Runtime directory is not accessible: …" when the Boundary Element module is started (fix pending B8).
- The Post-processing window does not open; the terminal shows "ImportError: cannot import name '_debian_h5py_mpi'" or "numpy.dtype size changed" (fix pending G6: Python packages that you installed with `pip install --user` for Python 3.12 hide those of the image). Workaround: start the image yourself with `PYTHONNOUSERSITE=1 singularity run --writable-tmpfs images/Postprocessing.sif`.
-->

## 9.3 Folders that the modules cannot find

The Boundary Element and the Post-processing modules find their inputs by the **names of the folders and files** written by the previous modules (chapters 4, 5 and 6). Most errors about inputs come from a folder that was renamed, or from the wrong level of folder.

| What you see | Module | Why | What to do |
|---|---|---|---|
| `Could not infer track contact condition from folder name:` followed by a name | Boundary Element | The name of the track folder does not end with `midSpan_nominal`, `quarterSpan_offsetIN`, … | Choose the folder of one contact case, and do not rename it (section 6.2) |
| `Could not infer wheel contact condition from folder name:` | Boundary Element | The name of the wheel folder does not end with `nominal`, `offsetIN` or `offsetOUT` | Choose the folder of one force position (section 6.2) |
| `FE parameters file not found:` followed by a path | Boundary Element | The folder does not contain `vert/parameters.json` (track) or `vertical/parameters.json` (wheel). You may have chosen the simulation folder instead of a contact case | Choose the folder of one contact case or force position |
| `No coordinate or displacement files found in the specified directory.` | Boundary Element | The folder `Outputs` does not hold the displacement fields | Check that the extraction of the rail and sleeper fields, or *Export displacement field for BEM*, was ticked when the structural model was computed |
| `BEM data file not found:` | Boundary Element | With *Use existing BE results*, the folder does not contain `bemData_….h5` | Choose the contact folder of the earlier BEM results (section 6.8) |
| `No valid wheel contact cases found.` or `No valid track contact cases found.`, with the list of the sub-folders found | Post-processing | The folders do not end with the contact names, or you chose a case folder instead of the simulation folder | Choose the folder that **contains** the contact case folders (section 7.2) |
| `Missing wheel file:` or `Missing track file:` followed by a path | Post-processing | A file listed in section 7.2 is missing in a contact case | Check that the calculation of that case finished, and that its folders were not moved |
| `Duplicate wheel contact case found: nominal` | Post-processing | Two folders of the wheelset folder end with the same contact name | Keep one folder for each contact name |
| `No valid acoustic transfer functions were found in the selected BEM results folders.` | Post-processing | The BEM folders do not follow the structure of section 7.2, or lack one of the two directions | Look at the table *Detected acoustic cases* of the Rolling noise tab |

## 9.4 Errors in a window of a module

These messages tell you which input to correct.

**Multi-Sleeper Model**

| What you see | What to do |
|---|---|
| `The total number of CPUs used (N) is larger than the number of CPUs available (M)` | Lower the number of jobs or of CPUs on the *Execution parameters* tab: jobs × CPUs must not exceed M (section 4.5) |
| `Please enter a correct number of jobs (1-M).` | The number of jobs must be between 1 and the number of cores |
| `The number of frequenciesis smaller than the number of jobs (=N).` | Enter at least as many frequencies as jobs (*Select frequencies…*) |
| `Please enter a correct working directory (reptrav).` | The working directory must already exist |
| `Saving directory was not found.` | Choose the results folder with *Select folder…* |
| `Please select at least one predefined force node.` | Tick at least one force position on the *Simulation setup* tab |
| `<name> already exists.` | A simulation with this name and this position is already in the list. Change the name, or remove it from the list |
| `Modes directory was not found.` or `Modes parameter file (JSON) was not found.` | With *Compute eigenmodes* unticked, choose a folder `Modes` that holds `parameters.json` (section 4.10) |
| `Pad material 1 Youngs modulus not defined.`, `Pad material 1 damping not defined.`, `Ballast Youngs modulus not defined.`, `Ballast damping not defined.` | Choose the four material files (section 4.6) |
| `Please enter a correct rail tilt, e.g. 1/40 or 0.025.` | Write the rail tilt as a fraction or a decimal number |
| `Rail projection mesh for BEM not defined.` | With a custom rail mesh and the rail extraction ticked, choose the projection mesh |

**Wheelset FE**

| What you see | What to do |
|---|---|
| `Simulation name must not contain spaces or path separators.` | Rename the simulation |
| `Output folder does not exist.` | Choose an existing folder inside your home directory |
| `Select at least one force node.` | Tick at least one force position |
| `Existing modes folder is required when Compute modes is unchecked.` | Choose the folder `Modes` of an earlier simulation |
| `Modes parameters file not found:` followed by a path | The folder that you chose is not a `Modes` folder |
| `Minimum frequency must be a number.` (or *Maximum*, *Density*, *Young's modulus*, *Poisson's ratio*) | Fill in the field with a number |

**Boundary Element**

| What you see | What to do |
|---|---|
| `Select at least one component to run.` | Switch on *Wheel*, *Rail* or *Sleepers* on the *Execution* tab |
| `Select at least one direction: Vertical or Lateral.` | Tick a direction on the *General* tab |
| `Track displacement folder is required.` (or *Wheel*, or *Track BEM results folder*) | Choose the folder on the *Track* or the *Wheel* tab |
| `Simulation name is required before adding to queue.`, `Output folder is required before adding to queue.` | Fill in the case name and the output folder |
| `n_substructures must be a positive odd integer.` | The number of rail or sleeper substructures must be odd |
| `Group name(s) [...] not found in …` followed by the available groups | A name in *Zero-velocity groups* does not exist in the mesh. Use one of the groups listed |
| `Custom receivers file must be .xlsx or .csv.` or `Custom receivers file must contain exactly 3 columns` | Fix the receiver file (section 6.3) |
| `Results already exist, but overwriting was not confirmed:` (row `Failed`) | Add the row to the queue again and confirm the overwriting, or choose another case name |

**Post-processing**

| What you see | What to do |
|---|---|
| `Case name is required.`, `Case name must not contain spaces or path separators.`, `Output folder does not exist.` | Correct the *General* tab |
| `Add at least one parameter set.` | Enter a speed and a load, and click **Add** (section 7.4) |
| `Select at least one roughness file.` | Choose a rail and/or a wheel roughness file, or untick *Roughness* |
| `Select roughness and/or pass-by in the Rolling noise tab.` | Tick *Roughness* or *Pass-by* |
| `Select at least one BEM results folder.` | Choose the BEM folders on the *Rolling noise* tab |
| `Manual FRF-file mode currently supports contact-force calculation only.` | With *Use FRF files*, switch on only *Calculate contact force* |
| `The existing contact-force folder cannot be the same as the output case folder.` | Choose another case name |
| `No frequency overlap, acoustic transfer functions: […], contact force: […]` | The BEM results and the contact force do not share any frequency. Check the frequency ranges of the earlier chapters |
| `Cannot calculate sound power without BEM data:` followed by a path | Untick *Calculate power*, or copy the file `bemData_….h5` next to `acouRes_….h5` (section 6.8) |

## 9.5 A calculation fails or never ends

| What you see | What it means | What to do |
|---|---|---|
| **Wheelset FE**: a row shows `Failed`, or the terminal shows a `FileNotFoundError` for a result file | Code_Aster did not produce the file | Open the `.mess` files (section 9.1) and read the first `<F>` or `<S>` line. The mesh or the groups of a custom mesh are the usual cause |
| **Wheelset FE**: `RuntimeError: Only N ring nodes found; insufficient for nMax=20` in a Code_Aster log | The wheel mesh has too few nodes on the ring through the contact node | Use a wheel mesh that is built by revolution (section 5.8) |
| **Wheelset FE**: a row shows `Done` but a result file is missing | The status does not always show a Code_Aster error | Always check the files (section 5.6) |
| **Multi-Sleeper Model**: `<line> / <vert or lat> did not run properly` in the terminal of the module | A calculation failed | Read the files of its folder `Messages`. Run again with *Debug mode*, to read the job windows |
| **Boundary Element**: `Substructure N failed.` followed by a trace | A calculation process failed | Read the trace in `log.txt`. If it mentions OpenCL, choose *numba* as the device interface (section 6.3) |
| **Boundary Element**: `Return code: -11`, `Possible segmentation fault.` in `error_message.txt` | The calculation ended abnormally. Running out of RAM can cause it with large calculations | Lower the numbers of workers (section 6.4) and run again |
| The computer becomes very slow, or a calculation is killed | Too many processes, or not enough RAM | Lower the numbers of jobs or workers. Check the RAM with `free -h` |
| **Post-processing**: `No Interaction.h5 files were found for acoustic scaling.` | The contact force was not computed, or its folder was moved | Switch on *Calculate contact force*, or choose an earlier case with *Use existing contact force* |
| **Post-processing**: `No result folders could be matched with the selected acoustic transfer functions.` | The contact cases and the BEM folders do not have the same names | Compare the names of the contact cases with the table *Detected acoustic cases* (section 7.2) |
| **Post-processing**: `No pass-by results were generated.` | There was no response file to combine | Run the steps before the pass-by first (section 7.6) |

## 9.6 The results look wrong

No program can say that a result is right. These checks find the most frequent mistakes.

- **A band is missing or empty in the noise spectra.** The frequency ranges of the track, the wheelset and the roughness files do not all cover it. The range of the results is the range that they **all** share (sections 4.7 and 7.9).
- **The levels are very different from what you expect.** Check the units: the track results are in mm and for 100 kN, the wheel results are in m and for 1 N (the Boundary Element module converts them). Check that the roughness file is in dB re 1 µm and that its wavelengths are in metres (section 7.5).
- **The pass-by has no sound before 100 Hz or after 5 kHz.** This is normal: the pass-by uses the bands from 100 Hz to 5 kHz.
- **The two directions give very different results.** Check that you computed **both** the vertical and the lateral direction in every module.
- **You changed an input and the result did not change.** You may have reused an earlier folder (*Use existing contact force*, *existing modes*, *existing BE results*). These options copy the earlier results.

## 9.7 Before you ask for help

Collect these elements. They answer most of the first questions.

1. **The messages**: the last 30 lines of the terminal window of the module, and, if there is one, the file `log.txt`, `error_message.txt` or `message_Stage2.mess` of the calculation.
2. **Your system**:

   ```bash
   lsb_release -ds
   singularity --version
   df -h ~
   free -h
   ```

3. **The version of the images**:

   ```bash
   for m in MultiSleeperModel WheelToolbox topnoisebem Postprocessing; do
     echo $m; singularity inspect images/$m.sif | grep build-date
   done
   ```

   **Expected result**: for each image, a line such as `org.label-schema.build-date: Monday_16_November_2026_14:7:27_CET`.
4. **What you did**: the module, the tab and the values that you entered. A picture of the window is the best way.

<!-- TODO: add the contact for help, as decided by the developers. -->
