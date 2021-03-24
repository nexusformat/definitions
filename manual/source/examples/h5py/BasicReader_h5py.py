#!/usr/bin/env python
'''Reads NeXus HDF5 files using h5py and plots the contents'''

import h5py as h5
import matplotlib.pyplot as plt
import os

f = h5.File('example.h5', 'r')
if 'default' in f.attrs:
  entry = f.attrs['default']
  if 'default' in f[entry].attrs:
    data = os.path.join(entry, f[entry].attrs['default'])
    print('Path to default plot is', data)
    if 'signal' in f[data].attrs:
      signal = os.path.join(data, f[data].attrs['signal'])
      rank = len(f[signal].shape)
      if rank > 2:
        z = f[signal][()][0]
      else:
        z = f[signal][()]
    axes = []
    labels = []
    if 'axes' in f[data].attrs:
      axis_list = f[data].attrs['axes']
      for axis in axis_list:
        axes.append(f[os.path.join(data, axis)][()]) 
        labels.append(axis)
  if rank == 1:
    plt.plot(z, axes[0])
  else:
    plt.imshow(z, extent=[axes[-1][0], axes[-1][-1], axes[-2][0], axes[-2][-1]])
  ax = plt.gca()
  ax.set_xlabel(labels[-1])
  if rank > 1:
    ax.set_ylabel(labels[-2])
  if 'title' in f[entry]:
    title = f[entry]['title'][()]
  elif 'title' in f[data]:
    title = f[data]['title'][()]
  ax.set_title(title)
  plt.colorbar()
