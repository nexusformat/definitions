"""
===============
Curve (1D Grid)
===============

Curve (not necessarily evenly spaced)

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
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("_mpl-gallery")

fig, ax = plt.subplots()

x = np.arange(10) ** 2
y1 = 4 + np.sin(2 * x)
y2 = 2 + np.sin(3 * x)
ax.plot(x, y1, "o-", label="y1")
ax.plot(x, y2, "go-", label="y2")

plt.show()
