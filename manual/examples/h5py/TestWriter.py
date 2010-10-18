
'''Writes a NeXus HDF5 file using h5py'''

import h5py    # HDF5 support
import time


if __name__ == '__main__':
    print "Write a NeXus HDF5 file"
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
    f = open('input.dat', 'r')
    TWO_COLUMNS = f.read()
    f.close()
    data = {'mr': [], 'I00': []}
    buffer = TWO_COLUMNS.strip().split("\n")
    for row in buffer:
        (x, y) = row.split()
        data['mr'].append(float(x))
        data['I00'].append(float(y))

    # create the HDF5 NeXus file
    f = h5py.File(fileName, "w")
    f.attrs['file_name'] = fileName
    f.attrs['creator'] = "Pete R. Jemian <jemian@anl.gov> using h5py"
    f.attrs['HDF5_Version'] = h5py.version.hdf5_version
    f.attrs['NeXus_version'] = "4.2.1"
    f.attrs['h5py_version'] = h5py.version.version
    f.attrs['file_time'] = timestamp
    f.attrs['file_update_time'] = timestamp

    nxentry = f.create_group("entry")
    nxentry.attrs["NX_class"] = "NXentry"   # identify NeXus base class

    # store the scan data
    nxdata = nxentry.create_group("mr_scan")
    nxdata.attrs["NX_class"] = "NXdata"   # identify NeXus base class

    mr = nxdata.create_dataset("mr", data=data['mr'])
    mr.attrs['units'] = "degrees"
    # tell NeXus this is first independent axis for plotting
    mr.attrs['primary'] = "1"   

    i00 = nxdata.create_dataset("I00", data=data['I00'])
    i00.attrs['units'] = "counts"
    # tell NeXus this is primary data for plotting
    i00.attrs['signal'] = "1"   

    # fill in some optional metadata
    nxentry.create_dataset("title", 
       data="APS USAXS instrument MR (alignment) scan")
    nxentry.create_dataset("start_time", data="2010-04-25T10:20:56-0500")
    nxentry.create_dataset("end_time", data="2010-04-25T10:21:16-0500")
    nxentry.create_dataset("experiment_identifier", 
       data="spec file 04_25.dat, scan #8")
    nxentry.create_dataset("experiment_description", 
       data="alignment scan of the USAXS collimating optics")

    # be CERTAIN to close the file
    f.close()

