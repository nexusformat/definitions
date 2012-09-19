#!/usr/bin/env python

'''
Print the structure of an HDF5 file to stdout

$Id$
'''


########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################


import h5py
import os
import sys
import getopt


class H5toText(object):
    '''
    Example usage showing default display::
    
        mc = H5toText(filename)
        mc.array_items_shown = 5
        mc.report()
    '''
    filename = None
    requested_filename = None
    isNeXus = False
    array_items_shown = 5

    def __init__(self, filename, makeReport = False):
        ''' Constructor '''
        self.requested_filename = filename
        if os.path.exists(filename):
            self.filename = filename
            self.isNeXus = self.testIsNeXus()
            if makeReport:
                self.report()

    def report(self):
        ''' reporter '''
        if self.filename == None: return
        f = h5py.File(self.filename, 'r')
        txt = self.filename
        if self.isNeXus:
            txt += ":NeXus data file"
        self.showGroup(f, txt, indentation = "")
        f.close()

    def testIsNeXus(self):
        ''' test if the selected HDF5 file is a NeXus file '''
        result = False
        try:
            f = h5py.File(self.filename, 'r')
            for value in f.itervalues():
                if str(type(value)) in ("<class 'h5py.highlevel.Group'>"):
                    if 'NX_class' in value.attrs:
                        v = value.attrs['NX_class']
                        if type(v) == type("a string"):
                            if v == 'NXentry':
                                result = True
                                break
            f.close()
        except:
            pass
        return result

    def showGroup(self, obj, name, indentation = "  "):
        '''print the contents of the group'''
        nxclass = ""
        if 'NX_class' in obj.attrs:
            class_attr = obj.attrs['NX_class']
            nxclass = ":" + str(class_attr)
        print indentation + name + nxclass
        self.showAttributes(obj, indentation)
        group_equivalents = (
	    "<class 'h5py.highlevel.File'>", 
	    "<class 'h5py.highlevel.Group'>", 
	    "<class 'h5py._hl.group.Group'>",
	)
        # show datasets (and links) first
        for itemname in sorted(obj):
            value = obj[itemname]
            if str(type(value)) not in group_equivalents:
                self.showDataset(value, itemname, indentation = indentation+"  ")
        # then show things that look like groups
        for itemname in sorted(obj):
            value = obj[itemname]
            if str(type(value)) in group_equivalents:
                self.showGroup(value, itemname, indentation = indentation+"  ")

    def showAttributes(self, obj, indentation = "  "):
        '''print any attributes'''
        for name, value in obj.attrs.iteritems():
            print "%s  @%s = %s" % (indentation, name, str(value))

    def showDataset(self, dset, name, indentation = "  "):
        '''print the contents and structure of a dataset'''
        shape = dset.shape
        if self.isNeXus:
            if "target" in dset.attrs:
                if dset.attrs['target'] != dset.name:
                    print "%s%s --> %s" % (indentation, name, dset.attrs['target'])
                    return
        txType = self.getType(dset)
        txShape = self.getShape(dset)
        if shape == (1,):
            value = " = %s" % str(dset[0])
            print "%s%s:%s%s%s" % (indentation, name, txType, txShape, value)
            self.showAttributes(dset, indentation)
        else:
	    print "%s%s:%s%s = __array" % (indentation, name, txType, txShape)
            self.showAttributes(dset, indentation)  # show these before __array
            if self.array_items_shown > 2:
                value = self.formatArray(dset, indentation + '  ')
                print "%s  %s = %s" % (indentation, "__array", value)
            else:
                print "%s  %s: %s" % (indentation, "__array", "not shown")

    def getType(self, obj):
        ''' get the storage (data) type of the dataset '''
        t = str(obj.dtype)
        if t[0:2] == '|S':
            t = 'char[%s]' % t[2:]
        if self.isNeXus:
            t = 'NX_' + t.upper()
        return t

    def getShape(self, obj):
        ''' return the shape of the HDF5 dataset '''
        s = obj.shape
        l = []
        for dim in s:
            l.append(str(dim))
        if l == ['1']:
            result = ""
        else:
            result = "[%s]" % ",".join(l)
        return result

    def formatArray(self, obj, indentation = '  '):
        ''' nicely format an array up to rank=5 '''
        shape = obj.shape
        r = ""
        if len(shape) in (1, 2, 3, 4, 5):
            r = self.formatNdArray(obj, indentation + '  ')
        if len(shape) > 5:
            r = "### no arrays for rank > 5 ###"
        return r

    def decideNumShown(self, n):
        ''' determine how many values to show '''
        if self.array_items_shown != None:
            if n > self.array_items_shown:
                n = self.array_items_shown - 2
        return n

    def formatNdArray(self, obj, indentation = '  '):
        ''' return a list of lower-dimension arrays, nicely formatted '''
        shape = obj.shape
        rank = len(shape)
        if not rank in (1, 2, 3, 4, 5): return None
        n = self.decideNumShown( shape[0] )
        r = []
        for i in range(n):
            if rank == 1: item = obj[i]
            if rank == 2: item = self.formatNdArray(obj[i, :])
            if rank == 3: item = self.formatNdArray(obj[i, :, :], indentation + '  ')
            if rank == 4: item = self.formatNdArray(obj[i, :, :, :], indentation + '  ')
            if rank == 5: item = self.formatNdArray(obj[i, :, :, :, :], indentation + '  ')
            r.append( item )
        if n < shape[0]:
            # skip over most
            r.append("...")
            #  get the last one
            if rank == 1: item = obj[-1]
            if rank == 2: item = self.formatNdArray(obj[-1, :])
            if rank == 3: item = self.formatNdArray(obj[-1, :, :], indentation + '  ')
            if rank == 4: item = self.formatNdArray(obj[-1, :, :, :], indentation + '  ')
            if rank == 5: item = self.formatNdArray(obj[-1, :, :, :, :], indentation + '  ')
            r.append( item )
        if rank == 1:
            s = str( r )
        else:
            s = "[\n" + indentation + '  '
            s += ("\n" + indentation + '  ').join(r)
            s += "\n" + indentation + "]"
        return s


if __name__ == '__main__':
    limit = 5
    filelist = []
    filelist.append('../Create/example1.hdf5')
    filelist.append('../Create/example2.hdf5')
    filelist.append('../Create/example3.hdf5')
    filelist.append('../Create/example4.hdf5')
    filelist.append('../../../NeXus/definitions/trunk/manual/examples/h5py/prj_test.nexus.hdf5')
    filelist.append('../../../NeXus/definitions/exampledata/code/hdf5/dmc01.h5')
    filelist.append('../../../NeXus/definitions/exampledata/code/hdf5/dmc02.h5')
    filelist.append('../../../NeXus/definitions/exampledata/code/hdf5/focus2007n001335.hdf')
    filelist.append('../../../NeXus/definitions/exampledata/code/hdf5/NXtest.h5')
    filelist.append('../../../NeXus/definitions/exampledata/code/hdf5/sans2009n012333.hdf')
    filelist.append('../Create/simple5.nxs')
    filelist.append('../Create/bad.h5')
    #filelist = []
    #filelist.append('testG.h5')
    #filelist.append('testG-pj.h5')
    if len(sys.argv) > 1:
        try:
            opts, args = getopt.getopt(sys.argv[1:], "n:")
        except:
            print
            print "SVN: $Id$"
            print "usage: ", sys.argv[0], " [-n ##] HDF5_file_name [another_HDF5_file_name]"
            print "  -n ## : limit number of displayed array items to ## (must be 3 or more or 'None')"
            print
        for item in opts:
            if item[0] == "-n":
                if item[1].lower() == "none":
                    limit = None
                else:
                    limit = int(item[1])
        filelist = args
    for item in filelist:
        mc = H5toText(item)
        mc.array_items_shown = limit
        mc.report()
