import numpy as np

def non_local_interaction_simulation(L, J=1.0):
    snapshot=[]
    for m in np.linspace(-1 , 1, 6):
        H_m = -J/2 * m**2 * L**2- m * np.random.choice([-1,1], (L,L))
        snapshot.append(H_m)

    return snapshot
