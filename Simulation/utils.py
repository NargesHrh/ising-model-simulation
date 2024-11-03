import numpy as np

def initialize_lattice(L):
    return np.random.choice([-1, 1], size=(L, L))


def get_neighbors(x, y, L):
    return [
        ((x + 1) % L, y), ((x - 1) % L, y),
        (x, (y + 1) % L), (x, (y - 1) % L)
    ]

def delta_E(lattice, i, j, L):
    spin = lattice[i, j]
    neighbors = sum(lattice[x, y] for x, y in get_neighbors(i, j, L))
    return 2 * spin * neighbors
