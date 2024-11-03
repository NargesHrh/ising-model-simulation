from .utils import delta_E
import numpy as np
def monte_carlo_step(lattice , i , j , T):
    dE = delta_E(lattice, i, j, lattice.shape[0])  # Calculate the energy difference


    if dE <= 0 or np.random.rand() < np.exp(-dE / T):
        lattice[i, j] *= -1  # Flip the spin
        return True
    return False




def run_metropolis(lattice , n_steps, snapshot_steps , T):
    snapshots = []

    for step in range(n_steps):
        i, j = np.random.randint(0, lattice.shape[0], size=2)
        monte_carlo_step(lattice, i, j, T)

        if step in snapshot_steps:
            snapshots.append(lattice.copy())
    return snapshots