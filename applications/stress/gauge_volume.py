import os
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")

origin = np.array([0, 0, 0])
x_dir = np.array([3, 0, 0])
y_dir = np.array([2, 2, 0])
z_dir = np.array([0, 0, 1.5])

# Gauge volume
verts = np.array(
    [
        origin,
        origin + x_dir,
        origin + x_dir + y_dir,
        origin + y_dir,
        origin + z_dir,
        origin + x_dir + z_dir,
        origin + x_dir + y_dir + z_dir,
        origin + y_dir + z_dir,
    ]
)

faces = [
    [verts[i] for i in [0, 1, 2, 3]],
    [verts[i] for i in [4, 5, 6, 7]],
    [verts[i] for i in [0, 1, 5, 4]],
    [verts[i] for i in [2, 3, 7, 6]],
    [verts[i] for i in [1, 2, 6, 5]],
    [verts[i] for i in [0, 3, 7, 4]],
]

ax.add_collection3d(
    Poly3DCollection(
        faces, facecolors="lightblue", linewidths=1.5, edgecolors="black", alpha=0.1
    )
)

# Coordinate system
arrow_opts = {"color": "red", "arrow_length_ratio": 0.1, "linewidth": 3}
xyz_origin = origin + 0.5 * x_dir + 0.5 * y_dir + 0.5 * z_dir
ax.quiver(*xyz_origin, *x_dir, **arrow_opts)
ax.quiver(*xyz_origin, *y_dir, **arrow_opts)
ax.quiver(*xyz_origin, *z_dir, **arrow_opts)

ax.text(*(xyz_origin + 1.05 * x_dir), "x", color="red", fontsize=24)
ax.text(*(xyz_origin + 1.05 * y_dir), "y", color="red", fontsize=24)
ax.text(*(xyz_origin + z_dir - 0.1 * y_dir), "z", color="red", fontsize=24)

# Gauge volume parameters
arrow_opts = {"color": "green", "arrow_length_ratio": 0.03, "linewidth": 3}
a_dir = x_dir + y_dir
ax.quiver(*origin, *a_dir, **arrow_opts)
ax.quiver(*a_dir, *-a_dir, **arrow_opts)

arrow_opts = {"color": "green", "arrow_length_ratio": 0.1, "linewidth": 3}
b_dir = x_dir - y_dir
ax.quiver(*y_dir, *b_dir, **arrow_opts)
ax.quiver(*(y_dir + b_dir), *-b_dir, **arrow_opts)

arrow_opts = {"color": "green", "arrow_length_ratio": 0.1, "linewidth": 3}
ax.quiver(*origin, *z_dir, **arrow_opts)
ax.quiver(*z_dir, *-z_dir, **arrow_opts)

ax.text(*(0.25 * a_dir - 0.05 * b_dir), "a", color="green", fontsize=24)
ax.text(*(y_dir + 0.35 * b_dir), "b", color="green", fontsize=24)
ax.text(*(z_dir - 0.25 * z_dir + 0.01 * a_dir), "c", color="green", fontsize=24)

# Plot
ax.view_init(elev=21, azim=-82)
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_zlim(0, 2)
ax.set_axis_off()
plt.tight_layout()
filename = os.path.join(os.path.dirname(__file__), "gauge_volume.png")
fig.savefig(filename, bbox_inches="tight", dpi=75)
plt.show()
