"""
Example usage of the banana-for-scale colormap.

Run with:
    python -m banana_for_scale
"""

import numpy as np
import matplotlib.pyplot as plt

# Importing registers the colormap
import banana_for_scale  # noqa: F401


def main():
    t = np.linspace(0, 2 * np.pi, 1024)
    data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]

    fig, ax = plt.subplots()
    im = ax.imshow(data2d, cmap="banana")

    fig.colorbar(im, ax=ax)
    plt.show()


if __name__ == "__main__":
    main()
