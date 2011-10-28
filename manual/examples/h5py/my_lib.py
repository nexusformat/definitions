#!/usr/bin/env python
'''
Library of routines to support NeXus HDF5 files using h5py
'''

import h5py    # HDF5 support

def makeFile(filename):
    """
    create and open an empty NeXus HDF5 file using h5py

    :param str filename: valid file name
    :return: h5py file object
    """
    return h5py.File(filename, "w")

def makeGroup(parent, name, nxclass):
    """
    create a NeXus group

    :param obj parent: parent group
    :param str name: valid NeXus group name
    :param str nxclass: valid NeXus class name
    :return: h5py group object
    """
    group = parent.create_group(name)
    group.attrs["NX_class"] = nxclass
    return group

def makeDataset(parent, name, data = None, attr = None):
    '''
    create and write data to a dataset in the HDF5 file hierarchy

    :param obj parent: parent group
    :param str name: valid NeXus dataset name
    :param obj data: the data to be saved
    :param dict attr: dictionary of attributes
    '''
    if data == None:
        obj = parent.create_dataset(name)
    elif type(data) == type("a string"):
	# pad strings with an extra space
	obj = parent.create_dataset(name, data=[data + " "])
    else:
        obj = parent.create_dataset(name, data=data)
    if attr:
        if type(attr) == type({}):
            # attr is a dictionary of attributes
            for k, v in attr.items():
                obj.attrs[k] = v
    return obj

def makeLink(parent, sourceObject, targetName):
    """
    create a NeXus link in an HDF5 file.

    :param obj parent: parent group of source
    :param obj sourceObject: HDF5 object
    :param str targetName: HDF5 node path string, such as /entry/data/data
    """
    if not 'target' in sourceObject.attrs:
        # NeXus-style link identifies full sourceObject HDF5 path
        sourceObject.attrs["target"] = str(sourceObject.name) # no unicode
    parent._id.link(sourceObject.name, targetName, h5py.h5g.LINK_HARD)


def get_2column_data(fileName):
    '''read two-column data from a file'''
    f = open(fileName,  'r')
    TWO_COLUMNS = f.read()
    f.close()

    xArr = []
    yArr = []
    buffer = TWO_COLUMNS.strip().split("\n")
    for row in buffer:
    	(x, y) = row.split()
    	xArr.append(float(x))
    	yArr.append(int(y))
    return xArr, yArr
