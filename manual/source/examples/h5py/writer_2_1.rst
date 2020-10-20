.. _Example-writer_2_1:

============================================================
``h5py`` example writing a simple NeXus data file with links
============================================================

Building on the previous example, we wish to identify our measured data with
the detector on the instrument where it was generated.
In this hypothetical case, since the detector was positioned at some
angle *two_theta*, we choose to store both datasets,
``two_theta`` and ``counts``, in a NeXus group.
One appropriate NeXus group is :ref:`NXdetector`.
This group is placed in a :ref:`NXinstrument` group
which is placed in a :ref:`NXentry` group.
To support a default plot, we provide a :ref:`NXdata` group.
Rather than duplicate the same data already placed in the detector group,
we choose to link to those datasets from the ``NXdata`` group.
(Compare the next figure with :ref:`fig.data-linking` in the
:ref:`Design` chapter of the NeXus User Manual.)
The :ref:`Design` chapter provides a figure
(:ref:`fig.data-linking`) with a small variation from our
previous example, placing the measured data
within the ``/entry/instrument/detector`` group.
Links are made from that data to the ``/entry/data`` group.

.. compound::

    .. _fig.writer_2_1:

    .. figure:: ../../img/ex_writer_2_1.png
        :alt: fig.writer_2_1
        :width: 80%

        h5py example showing linking in a NeXus file

The Python code to build an HDF5 data file with that structure (using
numerical data from the previous example) is shown below.

.. literalinclude:: writer_2_1.py
    :tab-width: 4
    :linenos:
    :language: python

It is interesting to compare the output of the ``h5dump``
of the data file ``writer_2_1.hdf5`` with our Python instructions.
See the *downloads* section below.

.. leave this out
   .. literalinclude:: writer_2_1_h5dump.txt
       :tab-width: 4
       :linenos:
       :language: text

Look carefully!  It *appears* in the output of
``h5dump`` that the actual data for ``two_theta``
and ``counts`` has *moved* into
the ``NXdata`` group at HDF5 path ``/entry/data``!  But we stored
that data in the ``NXdetector`` group at ``/entry/instrument/detector``.
This is normal for ``h5dump`` output.

A bit of explanation is necessary at this point.
The data is not stored in either HDF5 group directly.  Instead, HDF5
creates a ``DATA`` storage element in the file and posts a reference
to that ``DATA`` storage element as needed.
An HDF5 *hard link*
requests another reference to that same ``DATA`` storage element.
The ``h5dump`` tool describes in full that ``DATA`` storage element
the first time (alphabetically) it is called.  In our case, that is within the
``NXdata`` group.  The next time it is called, within the
``NXdetector`` group, ``h5dump`` reports that a hard link
has been made and shows the HDF5 path to the description.

NeXus recognizes this behavior of the HDF5 library and adds an additional structure
when building hard links, the ``target`` attribute,
to preserve the original location of the data.  Not that it actually matters.
the :ref:`punx tree <punx>` tool knows about the additional NeXus
``target`` attribute and shows the data to appear in its original
location, in the ``NXdetector`` group.

.. literalinclude:: writer_2_1_structure.txt
    :tab-width: 4
    :linenos:
    :language: text

downloads
*********

The Python code and files related to this section may be downloaded from the following table.

=====================================  =============================================
file                                   description
=====================================  =============================================
:download:`writer_2_1.py`              python code to write example *writer_2_1*
:download:`writer_2_1.hdf5`            NeXus file written by this code
:download:`writer_2_1_h5dump.txt`      *h5dump* analysis of the NeXus file
:download:`writer_2_1_structure.txt`   *punx tree* analysis of the NeXus file
=====================================  =============================================
    