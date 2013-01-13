#!/usr/bin/env python
'''
my_lib: routines to support reading & writing NeXus HDF5 files using h5py
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
    addAttributes(f, attr)
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
    addAttributes(obj, attr)
    return obj

def makeLink(parent, sourceObject, targetName):
    """
    create an internal NeXus (hard) link in an HDF5 file

    :param obj parent: parent group of source
    :param obj sourceObject: existing HDF5 object
    :param str targetName: HDF5 node path to be created, 
                            such as ``/entry/data/data``
    """
    if not 'target' in sourceObject.attrs:
        # NeXus link, NOT an HDF5 link!
        sourceObject.attrs["target"] = str(sourceObject.name)
    parent._id.link(sourceObject.name, targetName, h5py.h5g.LINK_HARD)

def makeExternalLink(hdf5FileObject, sourceFile, sourcePath, targetPath):
    """
    create an external link from sourceFile, sourcePath to targetPath in hdf5FileObject

    :param obj hdf5FileObject: open HDF5 file object
    :param str sourceFile: file containing existing HDF5 object at sourcePath
    :param str sourcePath: path to existing HDF5 object in sourceFile
    :param str targetPath: full node path to be created in current open HDF5 file, 
                            such as ``/entry/data/data``
                            
    .. note::
       Since the object retrieved is in a different file, 
       its ".file" and ".parent" properties will refer to 
       objects in that file, not the file in which the link resides.

    .. see:: http://www.h5py.org/docs-1.3/guide/group.html#external-links
    
    This routine is provided as a reminder how to do this simple operation.
    """
    hdf5FileObject[targetPath] = h5py.ExternalLink(sourceFile, sourcePath)

def addAttributes(parent, attr):
    """
    add attributes to an h5py data item

    :param obj parent: h5py parent object
    :param dict attr: dictionary of attributes
    """
    if attr and type(attr) == type({}):
        # attr is a dictionary of attributes
        for k, v in attr.items():
            parent.attrs[k] = v

def get2ColumnData(fileName):
    '''
    read two-column data from a file, 
    first column is float, 
    second column is integer
    '''
    buffer = numpy.loadtxt(fileName).T
    xArr = buffer[0]
    yArr = numpy.asarray(buffer[1],'int32')
    return xArr, yArr
