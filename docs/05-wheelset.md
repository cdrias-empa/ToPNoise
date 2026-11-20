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

**1 — Simulation name**  

Enter a name for the simulation. The name must not contain spaces or path separators (`/` or `\`).

The results are stored in a folder with this name inside the selected output folder.

**2 — Output folder**  

Select the folder where the simulation results will be stored.

**3 — Write MED**  

Select **Write MED** to additionally export the wheel response as MED files for visualization of the wheel surface vibration.

**4 — Compute modes**  

If **Compute modes** is selected, the wheelset modes are calculated.

**5 — Existing modes folder**  
If **Compute modes** is not selected, select an existing `Modes` folder. This allows previously calculated modes to be reused without repeating the modal calculation.
