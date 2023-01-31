"""Reads NeXus HDF5 files using h5py and prints the contents"""

import h5py  # HDF5 support


testFiles = ("simple_example_test.nexus.hdf5",)

GROUP_TYPE_MATCH = "<class 'h5py.highlevel.Group'>"
DATASET_TYPE_MATCH = "<class 'h5py.highlevel.Dataset'>"


def print_attr(parent, label):
    for k, v in parent.attrs.items():
        print("%s.attrs[%s]=%s" % (label, k, v))


def print_child(item, label):
    print("#" + "-" * 40)
    print("%s  %s" % (label, type(item)))
    print_attr(item, label)
    if repr(type(item)) == GROUP_TYPE_MATCH:
        base = label
        if "NX_class" in item.attrs:
            base += ":" + item.attrs["NX_class"]
        for k in item.keys():
            key = "%s/%s" % (base, k)
            print_child(item[k], key)
    if repr(type(item)) == DATASET_TYPE_MATCH:
        # print label, item.value
        print(label)
        print("shape:", item.shape)
        print("size:", len(item.shape))
        print("NumPy dtype:", item.dtype)


def process(fileName):
    try:
        f = h5py.File(fileName, "r")
    except Exception:
        return False
    try:
        print(f.filename)
        print("keys: ", f.keys())
        print_attr(f, "f")
        for k in f.keys():
            print_child(f[k], "%s://%s" % (fileName, k))
    finally:
        f.close()
    return True


if __name__ == "__main__":
    for fileName in testFiles:
        print("#" + "=" * 60)
        if not process(fileName):
            print("Could not open:", fileName)
