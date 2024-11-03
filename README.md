# 2D Ising Model Simulation

This project simulates a 2D Ising model using the Monte Carlo Metropolis algorithm. It includes local interactions (using the Metropolis algorithm). The simulation allows users to set custom lattice sizes, temperatures, and step counts, and it saves configuration snapshots and plots in a specified directory.

## Project Structure

ising-model-simulation

    ├── ising_model.py                  # Main script to run the simulation
    ├── simulation/
        ├── __init__.py                 # Initializes the package
        ├── local_interaction.py        # Simulates local interactions using the Metropolis algorithm
        ├── metropolis.py               # Contains the Monte Carlo step and Metropolis algorithm functions
        ├── plotter.py                  # Handles plotting and saving plots as .png files
        └── utils.py                    # Utility functions like energy calculation
    └── plots                           # Directory where plots are saved

## Key Components
* ising.model.py : The main script that prompts the user to input lattice size, temperature, and number of steps. It initializes the simulation, captures snapshots, and saves plots.

* `simulation/local_interaction.py`: Contains the local interaction simulation function (`local_interaction_simulation`), which initializes the lattice and runs the Metropolis algorithm for the specified number of steps.
* `simulation/metropolis.py`:
  * `monte_carlo_step`: A single Monte Carlo step that decides whether to flip a spin based on the Metropolis criterion.
  * `run_metropolis`: Runs the entire Metropolis algorithm, calling `monte_carlo_step` for each spin and capturing snapshots at specified intervals.
* `simulation/plotter.py`: Contains `plot_snapshots`, which plots the snapshots at different time steps and saves them to the `plots/` directory.
* `simulation/utils.py`: Utility functions used across simulations, like energy difference calculations (`delta_E`) and neighbor identification.

## Running
1. Set Up the Simulation Environment: Ensure you have `numpy` and `matplotlib` installed:
 
        pip install numpy matplotlib
2. Run the Simulation: Execute the main script:

        python ising_model.py
    The script will prompt for:

    * Lattice size (L): Defines the side length of the lattice (e.g., `20` for a `20x20` grid).
    * Temperature (T): Specifies the temperature for the Metropolis algorithm.
    * Steps (n_steps): Sets the number of Monte Carlo steps for the simulation.
3. Simulation Outputs:
    * Snapshots: Saved as images in the `plots/` directory, with configurations at various time steps.
    * Plots: Magnetization, energy, and free energy vs. temperature plots are generated and saved in the `plots/` directory.





