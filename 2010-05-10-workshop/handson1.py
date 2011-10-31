#!/usr/bin/python

import nxs

nf = nxs.open("hand1.h5", "w5")

nf.makegroup("entry","NXentry")
nf.opengroup("entry","NXentry")

nf.makegroup("data","NXdata")
nf.opengroup("data","NXdata")

nf.closegroup()


nf.makedata("hugo",'int32',[1])
nf.opendata("hugo")
nf.putdata(22.33)
nf.putattr("signal",1)

nxl = nf.getdataID()

nf.closedata()

nf.opengroup("data","NXdata")
nf.makelink(nxl)

nf.close()

exit
