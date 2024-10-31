from Simulation.local_interaction import local_interaction_simulation
from Simulation.non_local_interaction import non_local_interaction_simulation
from Simulation.plotter import plot_snapshots
import numpy as np

def main():
    L=int(input("Enter the length of the Lattice (e.g., 20 for a 20x20 grid):"))
    T=int(input("Enter the Temperature for the local interaction simulation:"))
    n_steps=int(input("Enter the number of steps for the Metropolis algorithm:"))

    snapshot_steps = np.linspace(0, n_steps, 6, dtype=int)

    local_snapshots = local_interaction_simulation(L, T, n_steps, snapshot_steps)
    plot_snapshots(local_snapshots, title="Local Interaction", filename=f"local_interaction_L{L}_T{T}")

    non_local_snapshots = non_local_interaction_simulation(L)
    plot_snapshots(non_local_snapshots, title="Non-Local Interaction", filename=f"non_local_interaction_L{L}")

    if __name__ == "__main__":
        main()
