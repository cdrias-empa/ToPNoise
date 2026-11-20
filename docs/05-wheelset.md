## 5.1 Overview

The Wheelset FE module calculates the **frequency response** of a railway wheelset.

### Assumptions

- The wheelset is modelled under **free boundary conditions**.
- The **rotation of the wheels is not taken into account**.

The calculation is carried out in two main steps:

1. calculation or reuse of the wheelset vibration modes;
2. calculation of the harmonic response for predefined wheel–rail contact positions.

The graphical interface is divided into three tabs:

- **General**
- **Modes and properties**
- **Execution**

The following sections describe these tabs.

## 5.2 General

The **General** tab defines the simulation name, the output location, and whether the wheelset modes are calculated or reused from a previous simulation.

![Wheelset FE — General tab](images/05-01-wheelset-general.png)

### Simulation name

Enter a name for the simulation. The name must not contain spaces or path separators (`/` or `\`).

The results are stored in a folder with this name inside the selected output folder.

### Output folder

Select the folder where the simulation results will be stored. The folder must already exist.

### Compute modes

If **Compute modes** is selected, the wheelset modes are calculated before the frequency response.

If **Compute modes** is not selected, an existing `Modes` folder must be provided. This allows previously calculated modes to be reused without repeating the modal calculation.

### Write MED

Select **Write MED** to additionally export the wheel response as MED files.

This option is used when the wheel-surface response is exported for the acoustic calculation.
