'''Writes a NeXus HDF5 file using h5py'''

import h5py    # HDF5 support
import six
import time


RAW_MR_SCAN = """
17.92608    1037
17.92591    1318
17.92575    1704
17.92558    2857
17.92541    4516
17.92525    9998
17.92508    23819
17.92491    31662
17.92475    40458
17.92458    49087
17.92441    56514
17.92425    63499
17.92408    66802
17.92391    66863
17.92375    66599
17.92358    66206
17.92341    65747
17.92325    65250
17.92308    64129
17.92291    63044
17.92275    60796
17.92258    56795
17.92241    51550
17.92225    43710
17.92208    29315
17.92191    19782
17.92175    12992
17.92158    6622
17.92141    4198
17.92125    2248
17.92108    1321
"""


if __name__ == '__main__':
    print("Write a NeXus HDF5 file")
    fileName = "prj_test.nexus.hdf5"
    tzsecs = abs(time.timezone)
    if time.timezone < 0:
        tzhhmm = "+"    # reverse logic, it seems
    else:
        tzhhmm = "-"
    if time.daylight:
        tzsecs -= 3600
    tzhhmm += "%02d%02d" % (tzsecs / 3600, (tzsecs % 3600)/60)
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%S") + tzhhmm

    # prepare the data
    data = {u"mr": [], u"I00": []}
    buffer = RAW_MR_SCAN.strip().split("\n")
    for row in buffer:
        (x, y) = row.split()
        data[u"mr"].append(float(x))
        data[u"I00"].append(float(y))

    # create the HDF5 NeXus file
    f = h5py.File(fileName, "w")
    f.attrs[u"file_name"] = fileName
    f.attrs[u"creator"] = "Pete R. Jemian <jemian@anl.gov> using h5py"
    f.attrs[u"HDF5_Version"] = six.u()h5py.version.hdf5_version
    f.attrs[u"NeXus_version"] = u"4.2.1"
    f.attrs[u"h5py_version"] = six.u(h5py.version.version)
    f.attrs[u"file_time"] = six.u(timestamp)
    f.attrs[u"file_update_time"] = six.u(timestamp)
    f.attrs[u"default"] = u"entry"    # identify default NXentry group

    nxentry = f.create_group(u"entry")
    nxentry.attrs[u"NX_class"] = u"NXentry"   # identify NeXus base class
    nxentry.attrs[u"default"] = u"mr_scan"    # identify default NXdata group

    # store the scan data
    nxdata = nxentry.create_group(u"mr_scan")
    nxdata.attrs[u"NX_class"] = u"NXdata"   # identify NeXus base class
    nxdata.attrs[u"signal"] = u"I00"        # identify default data to plot
    nxdata.attrs[u"axes"] = u"mr"           # identify default dimension scale to plot

    mr = nxdata.create_dataset(u"mr", data=data[u"mr"])
    mr.attrs[u"units"] = u"degrees"

    i00 = nxdata.create_dataset(u"I00", data=data[u"I00"])
    i00.attrs[u"units"] = u"counts"

    # fill in some optional metadata
    nxentry.create_dataset(u"title", 
    	data=u"APS USAXS instrument MR (alignment) scan")
    nxentry.create_dataset(u"start_time", data=u"2010-04-25T10:20:56-0500")
    nxentry.create_dataset(u"end_time", data=u"2010-04-25T10:21:16-0500")
    nxentry.create_dataset(u"experiment_identifier", 
       data=u"spec file 04_25.dat, scan #8")
    nxentry.create_dataset(u"experiment_description", 
       data=u"alignment scan of the USAXS collimating optics")

    # be CERTAIN to close the file
    f.close()
