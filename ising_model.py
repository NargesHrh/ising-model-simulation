import os
import numpy as np
import matplotlib.pyplot as plt

def get_neighbors(x, y, L):
    return [
        ((x + 1) % L, y), ((x - 1) % L, y),
        (x, (y + 1) % L), (x, (y - 1) % L)
    ]

def delta_E(lattice, i, j, J, L):
    spin = lattice[i, j]
    neighbors = sum(lattice[x, y] for x, y in get_neighbors(i, j, L))
    return 2 * J * spin * neighbors

# Local interaction (Metropolis algorithm)
def local_interaction_simulation(L, T, J, n_steps, snapshot_steps):
    lattice = np.random.choice([-1, 1], size=(L, L))
    snapshots = []

    for step in range(n_steps):
        i, j = np.random.randint(0, L, size=2)
        dE = delta_E(lattice, i, j, J, L)
        
        if dE <= 0 or np.random.rand() < np.exp(-dE / T):
            lattice[i, j] *= -1  # Flip spin

        if step in snapshot_steps:
            snapshots.append(lattice.copy())

    return snapshots

# Non-local interaction (Mean-field theory)
def non_local_interaction_simulation(L, J):
    snapshots = []
    for m in np.linspace(-1, 1, 6):  # Simulate 6 different states in mean-field theory
        H_m = -J / 2 * m**2 * L**2 - m * np.random.choice([-1, 1], (L, L))
        snapshots.append(H_m)
    
    return snapshots

# Plot snapshots and save to file
def plot_snapshots(snapshots, title, filename):
    # Create directory if it doesn't exist
    output_dir = "plots"
    os.makedirs(output_dir, exist_ok=True)
    
    # Plot and save
    fig, axes = plt.subplots(1, 6, figsize=(15, 3))
    for idx, ax in enumerate(axes):
        ax.imshow(snapshots[idx], cmap='coolwarm')
        ax.set_title(f"{title} {idx+1}")
        ax.axis('off')
    
    # Save the plot to the specified directory
    filepath = os.path.join(output_dir, f"{filename}.png")
    plt.savefig(filepath, format='png')
    plt.close()  # Close the figure to free memory
    print(f"Saved plot to {filepath}")

def main():
    # User inputs
    L = int(input("Enter the size of the lattice (e.g., 20 for a 20x20 grid): "))
    T = float(input("Enter the temperature for the local interaction simulation: "))
    J = 1.0  # Fixed interaction strength (can be made an input if desired)
    n_steps = int(input("Enter the number of steps for the Metropolis simulation: "))
    snapshot_steps = np.linspace(0, n_steps, 6, dtype=int)  # Capture 6 snapshots over the simulation

    # Run and plot snapshots for the local interaction
    local_snapshots = local_interaction_simulation(L, T, J, n_steps, snapshot_steps)
    plot_snapshots(local_snapshots, title="Local Interaction", filename=f"local_interaction_L{L}_T{T}")

    # Run and plot snapshots for the non-local interaction (mean-field theory)
    non_local_snapshots = non_local_interaction_simulation(L, J)
    plot_snapshots(non_local_snapshots, title="Non-Local Interaction", filename=f"non_local_interaction_L{L}")

# Execute the main function
if __name__ == "__main__":
    main()

