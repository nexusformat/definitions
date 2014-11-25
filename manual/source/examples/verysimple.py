#!/usr/bin/env python
# This example uses NeXpy to build the verysimple.nx5 data file.

from nexpy.api import nexus

angle = [18.9094, 18.9096, 18.9098, 18.91,  18.9102, 
         18.9104, 18.9106, 18.9108, 18.911, 18.9112, 
         18.9114, 18.9116, 18.9118, 18.912, 18.9122]
diode = [1193, 4474, 53220, 274310, 515430, 827880, 
         1227100, 1434640, 1330280, 1037070, 598720, 
         316460, 56677, 1000, 1000]

two_theta = nexus.SDS(angle, name="two_theta", 
               units="degrees", 
	       long_name="two_theta (degrees)")
counts = nexus.SDS(diode, name="counts", long_name="photodiode counts")
data = nexus.NXdata(counts,[two_theta])
data.save("verysimple.nx5")
