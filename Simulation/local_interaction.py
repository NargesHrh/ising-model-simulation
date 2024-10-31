import numpy as np
from utils import delta_E


def local_interaction_simulation(L,T,n_steps,snapshot_steps):
    lattice = np.random.choice([-1,1], size=(L,L))
    snapshot= []

    for step in range(n_steps):
        i, j=np.random.randint(0, L , size=2)
        dE = delta_E(lattice,i,j,L)

        if dE <= 0 or np.random.rand() < np.exp(-dE/T):
            lattice[i,j] *= -1
        if step in snapshot_steps:
            snapshot.append(lattice.copy())
    return snapshot
