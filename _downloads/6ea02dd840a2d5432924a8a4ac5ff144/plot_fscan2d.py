"""
==================
2D Continuous scan
==================

Data on a regular two-dimensional grid which is the combination
of an image and a histogram.

The x-axis defines the bin edges along the second dimension.
The y-axis defines the grid coordinates along the first dimension.

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
      @axes = ["y_set", "x_set"]
      @x_encoder_indices = [0, 1]
      @y_encoder_indices = 0
      @signal = "z"
      z: NX_FLOAT64[16,6]
      x_encoder: NX_FLOAT64[16,7]
      y_encoder: NX_FLOAT64[16]
      x_set: NX_FLOAT64[6]
      y_set: NX_FLOAT64[16]

Explanation:

1. ``@axes`` has two values which corresponds to the signal rank of two.

2. ``x_set`` and ``y_set`` are the default axes which can be used by readers
   that cannot handle multi-dimensional coordinates.

3. ``x_set_indices`` and ``y_set_indices`` are omitted because they would be equal to
   the position of ``"x_set"`` and ``"y_set"`` in ``@axes``.

4. The first dimension is spanned by three axes ``y_set``, ``y_encoder`` and ``x_encoder``.
   The axes ``y_set`` and ``y_encoder`` have as many values are there are data points
   along the first dimension. This is because the y motor moves one step after each scan
   of the x motor.

5. The second dimension is spanned by two axes ``x_set`` and ``x_encoder``. Since
   the x motor is scanned continuously, the encoder records the edge of every bin
   on which an data is recorded yielding 7 values instead of 6 along the second dimension.

6. The ``x_encoder`` spans the first dimensions because the actual x edges are slightly
   different for every x motion at each y position. Since the y motor does not move while
   scanning x, there is no need for ``y_encoder`` to span the second dimension because
   the value along this dimension remains constant.
"""

# Data
import numpy as np

x_set = np.linspace(-3, 3, 7)
y_set = np.linspace(-3, 3, 16)

rstate = np.random.RandomState(42)
noise_x = 0.1 * (x_set[1] - x_set[0])
noise_y = 0.1 * (y_set[1] - y_set[0])
x_encoder = x_set[np.newaxis, :] + rstate.normal(0, noise_x, (len(y_set), len(x_set)))
y_encoder = y_set + rstate.normal(0, noise_y, len(y_set))

nx = len(x_set) - 1
ny = len(y_set)
z = np.zeros((ny, nx))
xx = np.linspace(-3, 3, 200)
for i in range(ny):
    zi = (1 - xx / 2 + xx**5 + y_encoder[i] ** 3) * np.exp(-(xx**2) - y_encoder[i] ** 2)
    z[i, :], _ = np.histogram(xx, bins=x_encoder[i, :], weights=zi)

# Plot
import matplotlib.pyplot as plt  # noqa E402

plt.style.use("_mpl-gallery-nogrid")

fig, ax = plt.subplots()

y_set_new = np.empty_like(y_set, shape=(len(y_set) + 1,))
y_set_new[0] = 2 * y_set[0] - y_set[1]
y_set_new[1:-1] = (y_set[:-1] + y_set[1:]) / 2
y_set_new[-1] = 2 * y_set[-1] - y_set[-2]

mesh = ax.pcolormesh(x_set, y_set_new, z, linewidth=0.7)

plt.show()
