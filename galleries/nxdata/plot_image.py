"""
=====
Image
=====

Image on a regular two-dimensional grid.

The x-axis and y-axis define a regular 2D grid. The grid is equally spaced in
this example but this is not necessarily the case.

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
      x: NX_FLOAT64[16]
      y: NX_FLOAT64[30]
      z: NX_FLOAT64[30,16]

Explanation:

1. ``@axes`` has two values which corresponds to the signal rank of two.

2. ``z`` is the default signal to be plotted versus ``x`` and ``y``.
"""

# Data
import numpy as np

x = np.linspace(-3, 3, 16)
y = np.linspace(-3, 3, 30)

xx, yy = np.meshgrid(x, y)
z = (1 - xx / 2 + xx**5 + yy**3) * np.exp(-(xx**2) - yy**2)

# Plot
import matplotlib.pyplot as plt  # noqa E402

plt.style.use("_mpl-gallery-nogrid")

fig, ax = plt.subplots()

ax.imshow(z, origin="lower", aspect="auto")

plt.show()
