#!/usr/bin/python

import nxs

nf = nxs.open("hand1.h5", "r")

nf.opengroup("entry","NXentry")

for e in nf.entries():
  print e

nf.closedata()

nf.opendata('hugo')

val = nf.getdata()
print (val)
print(nf.getinfo())
for a in nf.attrs():
  print a

nf.closedata()


nf.close()

exit
