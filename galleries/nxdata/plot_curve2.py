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

# %%
# HDF5 example in Python.
import h5py
import numpy as np

with h5py.File("curve.h5", "w") as root:
    root.attrs["NX_class"] = "NXroot"
    scan1 = root.create_group("scan1")
    scan1.attrs["NX_class"] = "NXentry"
    data = scan1.create_group("data")
    data.attrs["NX_class"] = "NXdata"

    data.attrs["axes"] = ["x"]
    data.attrs["signal"] = "y1"
    data.attrs["auxiliary_signals"] = ["y2"]
    x = np.arange(10) ** 2
    data["x"] = x
    data["y1"] = 4 + np.sin(2 * x)
    data["y2"] = 2 + np.sin(3 * x)

# %%
# Plot example in Python.
import matplotlib.pyplot as plt

plt.style.use("_mpl-gallery")

fig, ax = plt.subplots()

with h5py.File("curve.h5", "r") as root:
    data = root["/scan1/data"]

    xname = data.attrs["axes"][0]
    yname1 = data.attrs["signal"]
    yname2 = data.attrs["auxiliary_signals"][0]

    x = data[xname][()]
    y1 = data[yname1][()]
    y2 = data[yname2][()]
    ax.plot(x, y1, "o-", label=yname1)
    ax.plot(x, y2, "go-", label=yname2)

plt.show()
