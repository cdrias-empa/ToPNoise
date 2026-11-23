## 6.1 Overview

The Boundary Elements Method (BEM) module calculates the acoustic radiation of the **rail, sleepers and wheel** from the vibration fields calculated with the FE models. Similar to the structural models, the acoustic calculation is carried out separately from the vibration field for **vertical and lateral unit forces**.

The main outputs **per component** are:

- **Acoustic pressure per unit force** at the defined receiver positions;
- **Radiated sound power per squared unit force**;
- **Radiation efficiency**;
- **Boundary solution** on the vibrating surface (boundary normal velocity and pressure), which can be reused to calculate the acoustic pressure at different receiver positions without repeating the BEM solution.

### Assumptions

- The acoustic radiation is calculated in **free field**. Ground reflections, ballast reflections and shielding are not taken into account.
- The **rail, sleepers and wheel are treated as independent acoustic radiators**.
- The acoustic model includes **one rail and one wheel** only.

The structural vibration field is first transferred from the FE surface mesh to the corresponding BEM mesh. The normal surface velocity is then calculated and used as boundary condition for the acoustic calculation. The resulting surface pressure is used to calculate the radiated sound power and the acoustic pressure at the receiver positions.

The calculation is therefore carried out in two main steps:

1. calculation of the BEM boundary solution from the structural vibration field;
2. calculation of the acoustic field at the selected receiver positions.

If an existing BEM boundary solution is used, only the second step is repeated.

For the **rail and sleepers**, the acoustic model is divided into several substructures which are calculated in parallel and combined afterwards. The **wheel** is calculated as a single structure and the calculation is parallelized over the frequency steps.

The graphical interface is divided into four tabs:

- **General**
- **Track**
- **Wheel**
- **Execution**
