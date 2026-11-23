## 6.1 Overview

The Boundary Elements Method (BEM) module calculates the acoustic radiation of the **rail, sleepers and wheel** from the vibration fields calculated with the FE models. Similar to the structural models, the acoustic calculation is carried out separately using the vibration fields obtained for **vertical and lateral unit forces**.

The main outputs **per component** are:

- **Acoustic pressure per unit force** at the defined receiver positions;
- **Radiated sound power per squared unit force**;
- **Radiation efficiency**;
- **Boundary solution** on the vibrating surface (boundary normal velocity and pressure), which can be reused to calculate the acoustic pressure at different receiver positions without repeating the BEM solution.

### Assumptions

- The acoustic radiation is calculated in **free field**. Propagation effects from the ground and ballast are not taken into account.
- The **rail, sleepers and wheel are treated as independent acoustic radiators**.
- The acoustic model includes **one rail and one wheel** only.

The structural vibration field is first transferred from the FE surface mesh to the corresponding BE mesh. The normal surface velocity is then used as boundary condition for the acoustic calculation. The resulting surface pressure is used to calculate the radiated sound power and the acoustic pressure at the receiver positions.

Internally, the calculation is therefore carried out in two main steps:

1. calculation of the BEM boundary solution from the structural vibration field;
2. calculation of the acoustic field at the selected receiver positions.

If an existing BEM boundary solution is used, only the second step is repeated.

The graphical interface is divided into four tabs:

- **General**
- **Track**
- **Wheel**
- **Execution**

## 6.2 General

The **General** tab defines the output location, receiver positions, computational backend and force directions used for the acoustic calculations.

![BEM — General tab](images/06-01-bem-general.png)

**1 — Output folder**  

Select the folder where the BEM results will be stored.

**2 — Receiver position**  

Select the receiver positions where the acoustic pressure is calculated. Two predefined measurement positions are available:

- **M75**: 7.5 m from the track centreline and 1.2 m above the rail head;
- **M3**: 3 m from the track centreline and 1.2 m above the rail head.

> [!NOTE]
> For both predefined positions, the receivers are distributed along a line parallel to the track from **−25 m to +25 m**, with a spacing of **0.1 m**. This array of receivers is used later to reconstruct the single-axle pass-by.

Select **Custom** to define other receiver positions.

**3 — Custom receiver**  

For custom receivers, select a `.csv` or `.xlsx` file without a header. Each row defines one receiver using three columns:

1. lateral distance from the track centreline [m];
2. height above the rail head [m];
3. longitudinal position relative to the centre of the model [m].

**4 — Device Interface**  

Select the computational backend used for the BEM calculation:

- **opencl**
- **numba**

**5–6 — Force direction**  

Select whether the acoustic response is calculated from the structural response to the **vertical**, **lateral**, or both unit forces. The two directions are calculated separately.
