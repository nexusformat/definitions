import numpy as np
from nexusformat.nexus import *


def write_nexus_file(fname, image, md={}):
    """
    write the image to a NeXus HDF5 data file

    Parameters
    ----------
    fname : str
        name of the file (relative or absolute) to be written
    image : numpy array
        the image data
    md : dictionary
        key: value where value is something that can be written by h5py
             (such as str, int, float, numpy array, ...)
    """
    nx = NXroot()
    nx['/entry'] = NXentry(NXinstrument(NXdetector()))
    nx['entry/instrument/detector/image'] = NXfield(image, units='counts',
                                                    compression='gzip')
    nx['entry/data'] = NXdata()
    nx['entry/data'].makelink(nx['entry/instrument/detector/image'])
    nx['entry/data'].nxsignal = nx['entry/data/image']

    if len(md) > 0:
        # /entry/instrument/metadata (optional, for metadata)
        metadata = nx['/entry/instrument/metadata'] = NXcollection()
        for k, v in md.items():
            metadata[k] = v

    nx.save(fname, 'w')

	
if __name__ == "__main__":
	"""demonstrate how to use this code"""
	import epics
	prefix = "13SIM1:"
	img = epics.caget(prefix+"image1:ArrayData")
	size_x = epics.caget(prefix+"cam1:ArraySizeX_RBV")
	size_y = epics.caget(prefix+"cam1:ArraySizeY_RBV")
	# edit the full image for just the binned data
	img = img[:size_x*size_y].reshape((size_x, size_y))

	extra_information = dict(
		unique_id = epics.caget(prefix+"image1:UniqueId_RBV"),
		size_x = size_x,
		size_y = size_y,
		detector_state = epics.caget(prefix+"cam1:DetectorState_RBV"),
		bitcoin_value="15000",
	)
	write_nexus_file("example.h5", img, md=extra_information)
