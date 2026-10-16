"""
=====
Curve
=====

One-dimensional curves as a function of the same axis.

The x-axis defines a regular 1D grid. As illustrated in this example,
the grid is not necessarily equally spaced.

.. code::

  @NX_class = "NXroot"
  @default = "scan1"
  scan1:NXentry
    @NX_class = "NXentry"
    @default = "data"
    data:NXdata
      @NX_class = "NXdata"
      @auxiliary_signals = ["y2"]
      @axes = ["x"]
      @signal = "y1"
      x:NX_INT64[10]
      y1:NX_FLOAT64[10]
      y2:NX_FLOAT64[10]

Explanation:

1. ``@axes`` has one value which corresponds to the signal rank of one.

2. ``y1`` is the default signal to be plotted versus ``x``.

3. ``y2`` is the only alternative signal to be plotted versus ``x``.
"""

# Data
import numpy as np

x = [0, 1, 8, 30, 35, 150, 200, 340, 500, 520]
y1 = 4 + np.sin(2 * np.array(x))
y2 = 2 + np.sin(3 * np.array(x))

# Plot
import matplotlib.pyplot as plt  # noqa E402

plt.style.use("_mpl-gallery")

fig, ax = plt.subplots()

ax.plot(x, y1, "o-", label="y1")
ax.plot(x, y2, "go-", label="y2")

plt.show()
