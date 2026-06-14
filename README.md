# MolMDTools

MolMDTools is a Python package for molecular structure analysis, molecular dynamics trajectory processing, hydrogen bond characterization, and preparation of quantum chemical calculations.

The package provides a unified object-oriented framework for working with molecular geometries, molecular dynamics trajectories, hydrogen-bonded systems, and computational chemistry workflows.

It was originally developed for the analysis of proton-transfer systems and hydrogen-bond networks obtained from quantum chemistry calculations and molecular dynamics simulations.

---

## Key Features

### Molecular Structures

- Atomic and molecular object representations
- Distance matrix generation
- Geometrical analysis:
  - interatomic distances
  - bond angles
  - torsion angles
- Center of mass calculations

### Molecular Dynamics Trajectories

- Reading and writing XYZ trajectories
- Trajectory manipulation and filtering
- Random frame selection
- Subsystem extraction
- Trajectory concatenation
- Center-of-mass alignment
- Periodic boundary condition handling

### Hydrogen Bond Analysis

- Hydrogen bond representation
- Automatic hydrogen bond detection
- Hydrogen bond trajectory analysis
- Collective variable calculations
- Distribution analysis of proton-transfer coordinates

### Quantum Chemistry Utilities

- Generation of Gaussian input files
- Support for geometry optimization jobs
- Frequency calculations
- NMR calculations

### Data Conversion

- LAMMPS dump → XYZ trajectory conversion

### Visualization

- Distance evolution plots
- Angle evolution plots
- Torsion angle evolution plots
- Collective variable analysis
- Publication-ready scientific figures

---

## Installation

```bash
pip install molmdtools
```

---

## Example: Reading an XYZ trajectory

```python
from molmdtools import XYZ_Trajectory

traj = XYZ_Trajectory.extr_from_xyz("trajectory.xyz")

print(f"Number of frames: {traj.steps_number}")
```

---

## Example: Center-of-Mass Alignment

```python
aligned_traj = traj.static_center_of_mass()
```

---

## Example: Hydrogen Bond Analysis

```python
from molmdtools import HB_Analyzer

frames_with_hbond = HB_Analyzer.hb_in_traj(
    traj,
    atoms_nums=[0, 1, 2]
)

print(frames_with_hbond)
```

---

## Example: Gaussian Input Generation

```python
from molmdtools import Calc_Data_Inp

calc = Calc_Data_Inp(
    molecule=molecule,
    method="B3LYP",
    basis="def2-TZVPD",
    opt=True,
    freq=True
)

calc.generate_gaussian_inp(
    path="inputs",
    filename="calculation.inp"
)
```

---

## Supported Formats

### Input

- XYZ trajectories
- XYZ molecular structures
- LAMMPS dump trajectories

### Output

- XYZ trajectories
- Gaussian input files

---

## Scientific Applications

MolMDTools is intended for:

- molecular dynamics trajectory analysis;
- hydrogen-bond characterization;
- proton-transfer studies;
- collective variable analysis;
- preparation of quantum chemistry calculations;
- post-processing of computational chemistry results.

---

## Author

### Vladimir Rogachevskii

Computational Chemistry Researcher

Email:
vladimir.rogachevskij@gmail.com

GitHub:
https://github.com/NCI-laboratory-SPb

---

## License

Distributed under the MIT License.