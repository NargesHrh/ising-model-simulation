from .metropolis import run_metropolis
from .utils import initialize_lattice


def local_interaction_simulation(L,T,n_steps,snapshot_steps):
    lattice = initialize_lattice(L)  # Initialize the lattice using the new function
    snapshots = run_metropolis(lattice, T, n_steps, snapshot_steps)
    return snapshots