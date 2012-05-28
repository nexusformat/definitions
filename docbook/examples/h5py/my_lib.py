#!/usr/bin/env python
'''
my_lib Library of routines to support NeXus HDF5 files using h5py
'''

import h5py    # HDF5 support
import numpy   # in this case, provides data structures

def makeFile(filename, **attr):
    """
    create and open an empty NeXus HDF5 file using h5py
    
    Any named parameters in the call to this method will be saved as
    attributes of the root of the file.
    Note that **attr is a dictionary of named parameters.

    :param str filename: valid file name
    :param attr: optional keywords of attributes
    :return: h5py file object
    """
    f = h5py.File(filename, "w")
    add_attributes(f, attr)
    return f

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

def makeDataset(parent, name, data = None, **attr):
    '''
    create and write data to a dataset in the HDF5 file hierarchy

    :param obj parent: parent group
    :param str name: valid NeXus dataset name
    :param obj data: the data to be saved
    :param attr: optional keywords of attributes
    '''
    if data == None:
        obj = parent.create_dataset(name)
    else:
        obj = parent.create_dataset(name, data=data)
    add_attributes(obj, attr)
    return obj

def makeLink(parent, sourceObject, targetName):
    """
    create a NeXus link in an HDF5 file.

    :param obj parent: parent group of source
    :param obj sourceObject: HDF5 object
    :param str targetName: HDF5 node path string, such as /entry/data/data
    """
    if not 'target' in sourceObject.attrs:
        # NeXus link, NOT an HDF5 link!
        sourceObject.attrs["target"] = str(sourceObject.name)
    parent._id.link(sourceObject.name, targetName, h5py.h5g.LINK_HARD)

def add_attributes(parent, attr):
    """
    add attributes to an h5py data item

    :param obj parent: h5py parent object
    :param dict attr: dictionary of attributes
    """
    if attr and type(attr) == type({}):
        # attr is a dictionary of attributes
        for k, v in attr.items():
            parent.attrs[k] = v

def get_2column_data(fileName):
    '''read two-column data from a file, first column is float, second column is integer'''
    buffer = numpy.loadtxt(fileName).T
    xArr = buffer[0]
    yArr = numpy.asarray(buffer[1],'int32')
    return xArr, yArr
