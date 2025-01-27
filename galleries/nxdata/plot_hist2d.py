"""
============
2D Histogram
============

Histogram on a regular two-dimensional grid.

The x-axis and y-axis define the bin edges. As illustrated in this example,
the bin widths are not necessarily identical.

.. code::

  @NX_class = "NXroot"
  @default = "scan1"
  scan1:
    @NX_class = "NXentry"
    @default = "data"
    data:
      @NX_class = "NXdata"
      @axes = ["y", "x"]
      @signal = "z"
      x: NX_FLOAT64[7]
      y: NX_FLOAT64[9]
      z: NX_FLOAT64[8,6]

Explanation:

1. ``@axes`` has two values which corresponds to the signal rank of two.

2. ``z`` is the default signal to be plotted versus ``x`` and ``y``.

3. ``z`` has 6 rows and 8 columns.

4. ``y`` has one more value than the first dimension of ``z`` since it contains the bin edges.

5. ``x`` has one more value than the second dimension of ``z`` since it contains the bin edges.
"""

# Data
import numpy as np

x = [-3.0, -2.5, -1.0, 0.0, 1.0, 2.5, 3.0]
y = [-3.0, -2.8, -1.3, -0.75, 0.0, 0.1, 1.5, 2.25, 3.0]

xx = np.linspace(-3, 3, 200)
yy = np.linspace(-3, 3, 200)
xx, yy = np.meshgrid(xx, yy)
zz = (1 - xx / 2 + xx**5 + yy**3) * np.exp(-(xx**2) - yy**2)
z, _, _ = np.histogram2d(yy.flatten(), xx.flatten(), bins=[y, x], weights=zz.flatten())

# Plot
import matplotlib.pyplot as plt  # noqa E402

plt.style.use("_mpl-gallery-nogrid")

fig, ax = plt.subplots()

mesh = ax.pcolormesh(x, y, z, edgecolor="k", linewidth=0.7, shading="flat")

plt.show()
