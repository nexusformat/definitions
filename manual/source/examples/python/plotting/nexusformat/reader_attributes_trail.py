from pathlib import Path
from nexusformat.nexus import nxopen

filename = str(
    Path(__file__).absolute().parent.parent
    / "simple_example_basic"
    / "simple_example_basic.nexus.hdf5"
)
with nxopen(filename) as f:
    # find the default NXdata group
    nx_data = f.get_default()
    signal = nx_data.nxsignal
    axes = nx_data.nxaxes[0]

nx_data.plot() # plot the data using Matplotlib

print(f"file: {f.nxfilename}")
print(f"signal: {signal.nxname}")
print(f"axes: {axes.nxname}")
print(f"{axes.nxname} {signal.nxname}")
for x, y in zip(axes, signal):
    print(x, y)
