import os
import matplotlib.pyplot as plt


def plot_snapshots(snapshots, title, filename):
    output_dir = "plots"
    os.makedirs(output_dir, exist_ok=True)

    fig, axes = plt.subplots(2, 3, figsize=(15, 3))
    for idx, ax in enumerate(axes):
        ax.imshow(snapshots[idx], cmap='cool.warm')
        ax.set_title(f"{title} {idx + 1}")
        ax.axis('off')

    filepath = os.path.join(output_dir, f"{filename}.png")
    plt.savefig(filepath, format='png')
    plt.close()
    print(f"Saved plot to {filepath}")
