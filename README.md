# Planisuss — Ecosystem Simulation

A Python-based ecosystem simulation in which different species interact within a shared environment, competing for resources and reproducing over time. The simulation models the evolution of the ecosystem across successive days and visualizes changes in its populations and vegetation.

## Overview

Planisuss is an interactive simulation of a simplified ecosystem. It models the relationships between organisms, their environment, and the resources they depend on for survival.

The simulation evolves in discrete time steps, representing successive days. During each step, the ecosystem changes through processes such as vegetation growth, organism movement, resource consumption, competition, and reproduction.

The project combines modular Python code, a graphical interface, and real-time visualization to explore how interactions between different species affect the evolution of an ecosystem.

## Features

- **Ecosystem simulation:** Model interactions between different organisms and their environment.
- **Multiple species:** Simulate vegetation, herbivores (*Erbasts*), and predators (*Carvizes*).
- **Dynamic population evolution:** Track how populations change over time through movement, resource consumption, reproduction, and competition.
- **Interactive controls:** Start, pause, resume, and adjust the simulation speed.
- **Spatial visualization:** Observe the ecosystem as it evolves on a two-dimensional map.
- **Statistical analysis:** Plot daily vegetation density, herbivore population, and predator population to analyze ecosystem dynamics.
- **Modular architecture:** Organize simulation logic into separate modules for species, environmental processes, configuration, and visualization.

## How It Works

The simulation progresses through a sequence of daily updates:

1. **Initialization:** Set up the environment, vegetation, herbivores, and predators.
2. **Vegetation growth:** Update the available vegetation.
3. **Movement:** Update the positions of organisms.
4. **Grazing:** Model herbivore interactions with vegetation.
5. **Competition and survival:** Resolve struggles between organisms.
6. **Reproduction:** Update the populations through reproduction.
7. **Visualization:** Refresh the ecosystem map and collect population statistics.

At the end of the simulation, the collected data is plotted to show how vegetation and animal populations evolved over time.

## Technologies

- **Python** — Core simulation logic and modular architecture.
- **Matplotlib** — Ecosystem visualization and population plots.
- **Tkinter** — Graphical interface and interactive simulation controls.

## Getting Started

### Prerequisites

- Python 3
- Matplotlib
- Tkinter, typically included with standard Python installations

### Installation

Clone the repository:

```bash
git clone https://github.com/MarcoMosconi/Planisuss.git
cd Planisuss
```

Install the required plotting library:

```bash
python -m pip install matplotlib
```

If Tkinter is not available in your Python installation, install it using your operating system's package manager.

### Run the Simulation

Start the application with:

```bash
python app.py
```

Use the graphical interface to configure and control the simulation. The simulation displays the evolving ecosystem and generates plots of vegetation density and animal populations.

## Project Structure

```text
Planisuss/
├── animals/        # Animal-related components
├── carvizes/       # Predator setup and logic
├── cells/          # Environment cell initialization
├── erbasts/        # Herbivore setup and logic
├── phases/         # Ecosystem simulation processes
├── vegetobs/       # Vegetation setup and logic
├── visualization/  # Visualization components
├── app.py          # Main application and simulation loop
├── interact.py     # Interactive controls
├── keygenerator.py # Key generation utilities
├── map.py          # Ecosystem map visualization
├── parameters.py   # Simulation parameters
└── README.md
```

## Documentation

The repository includes two documents providing additional information about the project:

- [`2022_23_planisuss_v0.95.pdf`](2022_23_planisuss_v0.95.pdf) — Project guidelines and requirements.
- [`Mosconi_MarcoMaria_517462.pdf`](Mosconi_MarcoMaria_517462.pdf) — Detailed project report describing the implementation and organization.
