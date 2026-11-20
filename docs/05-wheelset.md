## 5.1 Overview

The Wheelset FE module calculates the frequency response of a 3D railway wheelset. A **unit force** is applied at the wheel/rail contact in **vertical and lateral directions**. The main outputs are:

- **Driving-point FRFs** at the wheel–rail contact, used to calculate the wheel–rail interaction;
- **Vibration field over the wheel surface**, used to calculate the acoustic radiation with the Boundary Elements Method.

### Assumptions

- The wheelset is modelled under **free boundary conditions**.
- The **rotation of the wheels is not taken into account**.

The calculation is carried out in two main steps:

1. calculation or reuse of the wheelset vibration modes;
2. calculation of the harmonic response of the wheelset using modal superposition.

The graphical interface is divided into three tabs:

- **General**
- **Modes and properties**
- **Execution**

## 5.2 General

The **General** tab defines the simulation name, the output location, and whether the wheelset modes are calculated or reused from a previous simulation.

![Wheelset FE — General tab](images/05-01-wheelset-general.png)

**1 — Simulation name**  

Enter a name for the simulation. The name must not contain spaces or path separators (`/` or `\`).

The results are stored in a folder with this name inside the selected output folder.

**2 — Output folder**  

Select the folder where the simulation results will be stored.

**3 — Write MED**  

Select **Write MED** to additionally export the wheel response as MED files to visualize the wheelset surface vibration (can be read with ParaView for example).

**4 — Compute modes**  

If **Compute modes** is selected, the wheelset modes are calculated.

**5 — Existing modes folder**  
If **Compute modes** is not selected, select an existing `Modes` folder. This allows previously calculated modes to be reused without repeating the modal calculation.

## 5.3 Modes and properties

The **Modes and properties** tab defines the wheelset geometry, material properties and the settings used for the frequency response.

![Wheelset FE — Modes and properties tab](images/05-02-wheelset-modes.png)

**1 — Wheel geometry**  
Two predefined railway passenger wheels are available. Their geometries are shown below.

<p align="center">
  <img src="images/05-03-wheelset-geometry-small.png" alt="Wheelset 1 (small)" width="48%">
  <img src="images/05-04-wheelset-geometry-large.png" alt="Wheelset 2 (large)" width="48%">
</p>

<p align="center">
  <b>Wheelset 1 (small) - diameter 750 mm, left; Wheelset 2 (large) - diameter 920 mm, right.</b>
</p>

The reference coordinate system used in the FE models is:

- **X**: longitudinal direction (direction of travel);
- **Y**: vertical/radial direction;
- **Z**: lateral/axial direction.

Select **Custom** to use your own wheelset model. For a custom wheelset, select the FE wheel mesh and the corresponding projection mesh.

If an existing `Modes` folder is used, the wheel geometry and material properties are taken from the previous modal calculation and cannot be changed.

> [!NOTE]
> Using a **Custom** wheelset is an advanced option. Contact the developers for further information on how to prepare and configure a custom model.

**2 — Export displacement field for BEM**  
Select this option to export the response over the wheel surface for the subsequent Boundary Elements calculation. If it is not selected, only the driving-point FRFs at the selected contact positions are calculated.

The wheel surface response is exported on a dedicated **projection mesh**, which is used as the interface between the finite-Elements wheel model and the Boundary Elements model. The corresponding projection mesh is provided automatically for each predefined wheelset.

<p align="center">
  <img src="images/05-05-wheelset-projection-mesh-small.png" alt="Wheelset 1 (small)" width="48%">
  <img src="images/05-06-wheelset-projection-mesh-large.png" alt="Wheelset 2 (large)" width="48%">
</p>

<p align="center">
  <b>Projection meshes: Wheelset 1 (small), left; Wheelset 2 (large), right.</b>
</p>

**3 — FRF type**  
Select whether the frequency response is calculated as **Displacement**, **Velocity** or **Acceleration**.

**4 — Material properties**  
Define the density, Young's modulus and Poisson's ratio of the wheelset material. These properties are used when calculating the wheelset modes.

**5 — Damping**  
Two damping options are available:

- **Nominal**: the damping ratio is assigned according to the circumferential order of each mode.
- **Constant**: the value specified under **Zeta** is applied to all modes.

**6 — Force position**  
The different force positions are provided to account for variations in the lateral position of the wheel–rail contact as the train moves along the track. Select one or more wheel–rail contact positions on the wheel tread:

- **Nominal**: reference contact position, located **7 cm from the wheel flange**;
- **Offset-in**: located **1 cm inwards** from the nominal position (**towards the inner side of the wheelset**);
- **Offset-out**: located **1 cm outwards** from the nominal position (**towards the outer side of the wheelset**).

A separate simulation is added to the queue for each selected force position.

**7 — Frequency range**  
Set the minimum and maximum frequencies of the calculated frequency response. The modal basis is calculated to **1.5 times the maximum frequency** including the rigid-body motion.

## 5.4 Execution

![Wheelset FE — Execution tab](images/05-03-wheelset-execution.png)

**1 — Simulation queue**  
Shows the simulations added to the queue, the corresponding contact position and their current status.

**2 — Add to queue**  
Add the defined simulation to the queue. One simulation is added for each selected force position.

**3 — Start queue**  
Run the queued simulations sequentially. The status of each simulation changes from `Queued` to `Running` and then to `Done` or `Failed`.

**4 — Remove selected**  
Remove the selected simulations from the queue.

When **Compute modes** is selected, the modal basis is calculated for the first contact position and reused for the remaining contact positions.

## 5.5 Results

For a simulation called `wheel_study`, one folder is created for each selected wheel–rail contact position. The responses to the vertical and lateral unit forces are stored separately.

| Path | Content |
|---|---|
| `wheel_study/Modes/` | Modal basis of the wheelset |
| `wheel_study/nominal/` | Results for the nominal contact position |
| `wheel_study/offsetIN/` | Results for the inward contact position |
| `wheel_study/offsetOUT/` | Results for the outward contact position |
| `<contact position>/vertical/Outputs/` | Vertical harmonic-response results |
| `<contact position>/lateral/Outputs/` | Lateral harmonic-response results |

The main result files for each contact position are:

| File | Content |
|---|---|
| `vertical/Outputs/FRFcontact_vert.txt` | Driving-point FRFs for the vertical excitation |
| `lateral/Outputs/FRFcontact_lat.txt` | Driving-point FRFs for the lateral excitation |
| `vertical/Outputs/FRF_vert.txt` | Vibration field over the wheel surface for the vertical excitation |
| `lateral/Outputs/FRF_lat.txt` | Vibration field over the wheel surface for the lateral excitation |
| `parameters.json` | Parameters of the simulation |

The files `FRF_vert.txt` and `FRF_lat.txt` are generated when **Export displacement field for BEM** is selected and are used as input for the Boundary Elements calculation.

If **Write MED** is also selected, the vibration fields are additionally exported as:

- `vertical/Outputs/FRF_vert.med`
- `lateral/Outputs/FRF_lat.med`

The `Modes` folder contains:

- `fn.txt`: natural frequencies of the wheelset;
- `modes.med`: calculated mode shapes in MED format;
- `base_modes/`: modal basis used for the harmonic calculation;
- `parameters.json`: parameters used for the modal calculation.
