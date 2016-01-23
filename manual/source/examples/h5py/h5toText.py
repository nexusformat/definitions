#!/usr/bin/env python

'''
Print the structure of an HDF5 file to stdout
'''


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
        '''
        test if the selected HDF5 file is a NeXus file
        
        At this time, the code only tests for the existence of
        the NXentry group.  The tests should be extended 
        to require this structure be found::
	
          root
            NXentry
              NXdata
                @signal={dataset_name}
        	{dataset_name}:NX_numbers[]
	
        '''
        result = False
        try:
            f = h5py.File(self.filename, 'r')
            for value in f.itervalues():
                #print str(type(value))
                if '.Group' not in str(type(value)):
                    continue
                #print value.attrs.keys()
                if 'NX_class' not in value.attrs:
                    continue
                v = value.attrs['NX_class']
                #print type(v), v, type("a string")
                possible_types = ["<type 'numpy.string_'>", ]
                possible_types.append("<type 'str'>")
                if str(type(v)) not in possible_types:
                    continue
                if str(v) == str('NXentry'):
                    # TODO: apply more tests for required structure
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
        # show datasets and links next
        groups = []
        for itemname in sorted(obj):
            linkref = obj.get(itemname, getlink=True)
            if '.ExternalLink' in str(type(linkref)):
                # if the external file is not present, cannot know if
                # link target is a dataset or a group or another link
                fmt = '%s  %s --> file="%s", path="%s"'
                print fmt % (indentation, itemname, linkref.filename, linkref.path)
            else:
                classref = obj.get(itemname, getclass=True)
                value = obj.get(itemname)
                if '.File' in str(classref) or '.Group' in str(classref):
                    groups.append(value)
                elif '.Dataset' in str(classref):
                    self.showDataset(value, itemname, indentation+"  ")
                else:
                    msg = "unidentified %s: %s, %s", itemname, repr(classref), repr(linkref)
                    raise Exception, msg
        # then show things that look like groups
        for value in groups:
            itemname = value.name.split("/")[-1]
            self.showGroup(value, itemname, indentation+"  ")

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
                    print "%s%s --> %s" % (indentation, name, 
                                           dset.attrs['target'])
                    return
        txType = self.getType(dset)
        txShape = self.getShape(dset)
        if shape == (1,):
            value = " = %s" % str(dset[0])
            print "%s%s:%s%s%s" % (indentation, name, txType, 
                                   txShape, value)
            self.showAttributes(dset, indentation)
        else:
	    print "%s%s:%s%s = __array" % (indentation, name, 
                                       txType, txShape)
            # show these before __array
            self.showAttributes(dset, indentation)
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
            if rank == 3: item = self.formatNdArray(obj[i, :, :], 
                                                    indentation + '  ')
            if rank == 4: item = self.formatNdArray(obj[i, :, :, :], 
                                                    indentation + '  ')
            if rank == 5: item = self.formatNdArray(obj[i, :, :, :, :], 
                                                    indentation + '  ')
            r.append( item )
        if n < shape[0]:
            # skip over most
            r.append("...")
            #  get the last one
            if rank == 1: item = obj[-1]
            if rank == 2: item = self.formatNdArray(obj[-1, :])
            if rank == 3: item = self.formatNdArray(obj[-1, :, :], 
                                                    indentation + '  ')
            if rank == 4: item = self.formatNdArray(obj[-1, :, :, :], 
                                                    indentation + '  ')
            if rank == 5: item = self.formatNdArray(obj[-1, :, :, :, :], 
                                                    indentation + '  ')
            r.append( item )
        if rank == 1:
            s = str( r )
        else:
            s = "[\n" + indentation + '  '
            s += ("\n" + indentation + '  ').join(r)
            s += "\n" + indentation + "]"
        return s


def do_filelist(filelist, limit=5):
    '''
    interpret the structure of a list of HDF5 files
    
    :param [str] filelist: one or more file names to be interpreted
    :param int limit: maximum number of array items to be shown (default = 5)
    '''
    for item in filelist:
        mc = H5toText(item)
        mc.array_items_shown = limit
        mc.report()


def do_test():
    limit = 3
    filelist = []
    filelist.append('th02c_ps02_1_master.h5')
    filelist.append('external_angles.hdf5')
    filelist.append('external_counts.hdf5')
    filelist.append('external_master.hdf5')
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
    
    do_filelist(filelist, limit)


def main():
    '''standard command-line interface'''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "n:")
    except:
        print
        print "usage: ", sys.argv[0], " [-n ##] HDF5_file_name [another_HDF5_file_name]"
        print "  -n ## : limit number of displayed array items to ## (must be 3 or more or 'None')"
        print
    for item in opts:
        if item[0] == "-n":
            if item[1].lower() == "none":
                limit = None
            else:
                limit = int(item[1])
    do_filelist(args)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        do_test()
