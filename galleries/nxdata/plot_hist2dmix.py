"""
==================
2D Mixed-Histogram
==================

Data on a regular two-dimensional grid which is the combination
of an image and a histogram.

The x-axis defines the bin edges along the second dimension.
The y-axis defines the grid coordinates along the first dimension.

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
      y: NX_FLOAT64[16]
      z: NX_FLOAT64[16,6]

Explanation:

1. ``@axes`` has two values which corresponds to the signal rank of two.

2. ``z`` is the default signal to be plotted versus ``x`` and ``y``.

3. ``z`` has 16 rows and 6 columns.

4. ``x`` has one more value than the second dimension of ``z`` since it contains the bin edges.
"""

# Data
import numpy as np

x = [-3.0, -2.5, -1.0, 0.0, 1.0, 2.5, 3.0]
y = np.linspace(-3, 3, 16)

nx = len(x) - 1
ny = len(y)
z = np.zeros((ny, nx))
xx = np.linspace(-3, 3, 200)
for i in range(ny):
    zi = (1 - xx / 2 + xx**5 + y[i] ** 3) * np.exp(-(xx**2) - y[i] ** 2)
    z[i, :], _ = np.histogram(xx, bins=x, weights=zi)

# Plot
import matplotlib.pyplot as plt  # noqa E402

plt.style.use("_mpl-gallery-nogrid")

fig, ax = plt.subplots()

y_new = np.empty_like(y, shape=(len(y) + 1,))
y_new[0] = 2 * y[0] - y[1]
y_new[1:-1] = (y[:-1] + y[1:]) / 2
y_new[-1] = 2 * y[-1] - y[-2]

mesh = ax.pcolormesh(x, y_new, z, linewidth=0.7)

plt.show()
