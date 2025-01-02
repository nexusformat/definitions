"""
==================
2D Mixed-Histogram
==================

Data on a regular two-dimensional grid which is the combination
of an image and a histogram.

The x-axis defines the bin edges along the first dimension.
The y-axis defines the grid coordinates along the second dimension.

.. code::

  @NX_class = "NXroot"
  @default = "scan1"
  scan1:
    @NX_class = "NXentry"
    @default = "data"
    data:
      @NX_class = "NXdata"
      @axes = ["x", "y"]
      @signal = "z"
      x: NX_FLOAT64[7]
      y: NX_FLOAT64[16]
      z: NX_FLOAT64[6,16]

Explanation:

1. ``@axes`` has two values which corresponds to the signal rank of two.

2. ``z`` is the default signal to be plotted versus ``x`` and ``y``.

3. ``x`` has one more value than the first dimension of ``z`` since it contains the bin edges.
"""

# Data
import numpy as np

x = [-3.0, -2.5, -1.0, 0.0, 1.0, 2.5, 3.0]
y = np.linspace(-3, 3, 16)

xx = np.linspace(-3, 3, 200)
yy = np.linspace(-3, 3, 200)
xx, yy = np.meshgrid(xx, yy)
zz = (1 - xx / 2 + xx**5 + yy**3) * np.exp(-(xx**2) - yy**2)
y_edges = np.linspace(-3, 3, len(y) + 1)
z, _, _ = np.histogram2d(
    xx.flatten(), yy.flatten(), bins=[x, y_edges], weights=zz.flatten()
)

# Plot
import matplotlib.pyplot as plt  # noqa E402

plt.style.use("_mpl-gallery-nogrid")

fig, ax = plt.subplots()
mesh = ax.pcolormesh(x, y_edges, z.T, linewidth=0.7)

plt.show()
