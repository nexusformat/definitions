#!/usr/bin/env python
'''uses h5py to build the verysimple.nx5 data file'''

import h5py

angle = [18.9094, 18.9096, 18.9098, 18.91,  18.9102, 
         18.9104, 18.9106, 18.9108, 18.911, 18.9112, 
         18.9114, 18.9116, 18.9118, 18.912, 18.9122]
diode = [1193, 4474, 53220, 274310, 515430, 827880, 
         1227100, 1434640, 1330280, 1037070, 598720, 
         316460, 56677, 1000, 1000]

f = h5py.File('verysimple.nx5', 'w')
f.attrs['default'] = 'entry'

nxentry = f.create_group('entry')
nxentry.attrs["NX_class"] = 'NXentry'
nxentry.attrs['default'] = 'data'

nxdata = nxentry.create_group('data')
nxdata.attrs["NX_class"] = 'NXdata'
nxdata.attrs['signal'] = 'counts'
nxdata.attrs['axes'] = 'two_theta'
nxdata.attrs['two_theta_indices'] = [0,]

tth = nxdata.create_dataset('two_theta', data=angle)
tth.attrs['units'] = 'degrees'
tth.attrs['long_name'] = 'two_theta (degrees)'

counts = nxdata.create_dataset('counts', data=diode)
counts.attrs['units'] = 'counts'
counts.attrs['long_name'] = 'photodiode counts'

f.close()
