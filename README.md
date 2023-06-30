# CellAutomatonModel

This project is a package that enables the computation of cellular automaton models. Cellular automaton models can perform calculations based on any type of rule and support output as both text and diagrams.

## Features

- Computation of cellular automaton models for any rule
- Support for output as text and diagrams
- Simple and user-friendly interface

## Installation

Clone the repository using the following command:

```bash
git clone https://github.com/SoraKurihara/CellAutomatonModel.git
```

## Usage
```
Rule = 90
L = 101

# X       = np.random.choice([0,1], size=L)
X = np.zeros(L)
X[int(L / 2)] = 1

# CA = CellAutomatonModel(Rule, Boundary="Fix")
CA = CellAutomatonModel(Rule, Boundary="Periodic")
Cells = CA.CA(X, 101)
CA.print(Cells)
CA.plot(Cells, DIR="01_Simulation/Output/")
```

# Author

* Sora Kurihara
* Kansai University
* sorasorasora.918@gmail.com
