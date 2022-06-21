import numpy as np
import h5py
import datetime

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
	nexus = h5py.File(fname, "w")
	nexus.attrs["filename"] = fname
	nexus.attrs["file_time"] = datetime.datetime.now().astimezone().isoformat()
	nexus.attrs["creator"] = "write_nexus_file()"
	nexus.attrs["H5PY_VERSION"] = h5py.__version__

	# /entry
	nxentry = nexus.create_group("entry")
	nxentry.attrs["NX_class"] = "NXentry"
	nexus.attrs["default"] = nxentry.name

	# /entry/instrument
	nxinstrument = nxentry.create_group("instrument")
	nxinstrument.attrs["NX_class"] = "NXinstrument"

	# /entry/instrument/detector
	nxdetector = nxinstrument.create_group("detector")
	nxdetector.attrs["NX_class"] = "NXdetector"

	# /entry/instrument/detector/image
	ds = nxdetector.create_dataset("image", data=image, compression="gzip")
	ds.attrs["units"] = "counts"
	ds.attrs["target"] = "/entry/instrument/detector/image"

	# /entry/data
	nxdata = nxentry.create_group("data")
	nxdata.attrs["NX_class"] = "NXdata"
	nxentry.attrs["default"] = nxdata.name

	# /entry/data/data --> /entry/instrument/detector/image
	nxdata["data"] = nexus["/entry/instrument/detector/image"]
	nxdata.attrs["signal"] = "data"

	if len(md) > 0:
		# /entry/instrument/metadata (optional, for metadata)
		metadata = nxinstrument.create_group("metadata")
		metadata.attrs["NX_class"] = "NXcollection"
		for k, v in md.items():
			try:
				metadata.create_dataset(k, data=v)
			except Exception:
				metadata.create_dataset(k, data=str(v))

	nexus.close()

	
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
