
'''Writes a NeXus HDF5 file using h5py'''

import h5py    # HDF5 support

if __name__ == '__main__':
    print "Write a NeXus HDF5 file"
    fileName = "prj_test.nexus.hdf5"
    timestamp = "2010-10-18T17:17:04-0500"

    # prepare the data
    f = open('input.dat', 'r')
    TWO_COLUMNS = f.read()
    f.close()
    data = {'mr': [], 'I00': []}
    buffer = TWO_COLUMNS.strip().split("\n")
    for row in buffer:
        (x, y) = row.split()
        data['mr'].append(float(x))
        data['I00'].append(int(y))

    # create the HDF5 NeXus file
    f = h5py.File(fileName, "w")
    f.attrs['file_name'] = fileName
    f.attrs['file_time'] = timestamp
    f.attrs['creator'] = "$Id$"
    f.attrs['HDF5_Version'] = h5py.version.hdf5_version
    f.attrs['NeXus_version'] = "4.3.0"
    f.attrs['h5py_version'] = h5py.version.version
    f.attrs['instrument'] = "APS USAXS at 32ID-B"

    nxentry = f.create_group("entry")
    nxentry.attrs["NX_class"] = "NXentry"   # identify NeXus base class

    # store the scan data
    nxdata = nxentry.create_group("mr_scan")
    nxdata.attrs["NX_class"] = "NXdata"   # identify NeXus base class

    mr = nxdata.create_dataset("mr", data=data['mr'])
    mr.attrs['NAPItype'] = "NX_%s[%d]" % (str(mr.dtype).upper(), len(data['mr']))
    mr.attrs['units'] = "degrees"
    # tell NeXus this is first independent axis for plotting
    mr.attrs['primary'] = "1"    

    i00 = nxdata.create_dataset("I00", data=data['I00'])
    i00.attrs['NAPItype'] = "NX_%s[%d]" % (str(i00.dtype).upper(), len(data['I00']))
    i00.attrs['units'] = "counts"
    # tell NeXus this is primary data for plotting
    i00.attrs['signal'] = "1"

    # be CERTAIN to close the file
    f.close()

