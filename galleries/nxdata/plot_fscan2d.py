"""
==================
2D Continuous scan
==================

Data on a regular two-dimensional grid which is the combination
of an image and a histogram.

The x-axis defines the bin edges along the first dimension.
The y-axis defines the grid coordinates along the second dimension.

This is a typical 2D scanning example where a sample is scanned through
a focussed X-ray beam in two dimensions. The x motor is scanned continuously
and both motors have an encoder which records the actual motor position as
opposed to the requested or `set` position.

.. code::

  @NX_class = "NXroot"
  @default = "scan1"
  scan1:
    @NX_class = "NXentry"
    @default = "data"
    data:
      @NX_class = "NXdata"
      @axes = ["x_set", "y_set"]
      @x_encoder_indices = [0, 1]
      @y_encoder_indices = 1
      @signal = "z"
      z: NX_FLOAT64[10,16]
      x_encoder: NX_FLOAT64[11,16]
      y_encoder: NX_FLOAT64[16]
      x_set: NX_FLOAT64[10]
      y_set: NX_FLOAT64[16]

Explanation:

1. ``@axes`` has two values which corresponds to the signal rank of two.

2. ``x_set`` and ``y_set`` are the default axes which can be used by readers
    that cannot handle multi-dimensional coordinated.

3. ``x_set_indices`` and ``y_set_indices`` are omitted because they would be equal to
    the position of ``"x_set"`` and ``"y_set"`` in ``@axes``.

4. The first dimension is spanned by two axes ``x_set`` and ``x_encoder``. Since
    the x motor is scanned continuously, the encoder records the edge of every bin
    on which an data is recorded yielding 11 values instead of 10 along the
    first dimension. The ``x_encoder`` spans two dimensions because the actual x edges
    are slightly different for every x motion at each y position.

5. The second dimension is spanned by two axes ``y_set`` and ``y_encoder``. The axes
    have as many values are there are data points along the second dimension. This is
    because the y motor moves one step after each scan of the x motor. Since the y
    motor does not move while scanning x, there is no need for ``y_encoder`` to span
    the first dimension because the value along this dimension remains constant.
"""

# Data
import numpy as np

x_set = np.linspace(-3, 3, 11)
y_set = np.linspace(-3, 3, 16)

rstate = np.random.RandomState(42)
x_encoder = x_set[:, np.newaxis] + rstate.normal(0, 0.1, (11, 16))
y_encoder = y_set + rstate.normal(0, 0.1, 16)

xx = np.linspace(-3, 3, 200)
yy = y_encoder
xx, yy = np.meshgrid(xx, yy)
z_raw = (1 - xx / 2 + xx**5 + yy**3) * np.exp(-(xx**2) - yy**2)

nx = len(x_set) - 1
ny = len(y_set)
z = np.zeros((nx, ny))
for j, (xj, zj) in enumerate(zip(xx, z_raw)):
    for i in range(nx):
        mask = (xj >= x_set[i]) & (xj < x_set[i + 1])
        z[i, j] = np.sum(zj[mask])

# Plot
import matplotlib.pyplot as plt  # noqa E402

plt.style.use("_mpl-gallery-nogrid")

fig, ax = plt.subplots()
ax.imshow(z.T, origin="lower", aspect="auto")

plt.show()
