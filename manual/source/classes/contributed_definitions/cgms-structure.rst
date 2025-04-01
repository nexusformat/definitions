.. _CgmsFeatures-Structure:

=========================
Geometry & Microstructure
=========================

.. index::
   CgmsBC

.. _CgmsBC:

Base Classes
############

The following base classes are defined to incentivize the use of NeXus for
using computational-geometry-based descriptions. In what follows, base classes
for frequently used shapes and geometric primitives are proposed:

    :ref:`NXcg_primitive`:
        Base class from which most other NXcg classes that define specific primitives inherit.

    :ref:`NXcg_ellipsoid`:
        A description for a set of possibly dissimilar oriented ellipsoids.

    :ref:`NXcg_cylinder`:
        A description for a set of possibly dissimilar oriented cylinders.

    :ref:`NXcg_point`:
        A collection of points with labels.

    :ref:`NXcg_polyline`:
        A collection of lines and linear segments.

    :ref:`NXcg_triangle`:
        A collection of triangles.

    :ref:`NXcg_parallelogram`:
        A collection of possibly dissimilar parallelograms.

    :ref:`NXcg_polygon`:
        A collection of polygons.

    :ref:`NXcg_polyhedron`:
        A collection of polyhedra.

    :ref:`NXcg_roi`:
        A container to host a number of different types of primitives.

    :ref:`NXcg_tetrahedron`:
        A collection of tetrahedra.

    :ref:`NXcg_hexahedron`:
        A collection of hexahedra with capabilities to represent
        also simpler (bounding) boxes for e.g. binary trees.

These base classes describe data structures used for more complex geometries:

    :ref:`NXcg_face_list_data_structure`:
        In essence, the usual way how polygon/polyhedra data are reported:
        A list of vertices and faces with identifier and properties.

    :ref:`NXcg_half_edge_data_structure`:
        A half-edge data structure (also known as a doubly connected edge list)
        is a useful complementary descriptor for polygon/polyhedra which enables
        topological analyses and traversal of the graph of how polygons and
        polyhedra are connected.

    :ref:`NXcg_unit_normal`:
        As an additional structuring element especially for meshes, well-documented
        normal information is crucial for distance computations.

    :ref:`NXcg_alpha_complex`:
        Alpha shapes and alpha wrappings, specifically the special case of the
        convex hull, are frequently used geometrical models for describing
        a boundary or edge to a set of geometric primitives.

Next, a few base classes are defined for documenting discretized representations
of material (area or volume) which can be useful not only for stencil-based methods:

    :ref:`NXcg_grid`:
        A grid of cells.

    :ref:`NXisocontour`:
        A description for isocontour descriptions.

    :ref:`NXdelocalization`:
        An approach to document procedures whereby a scalar field
        is smoothed in a controlled manner.

    :ref:`NXsimilarity_grouping`:
        An alternative for NXclustering.

    :ref:`NXclustering`:
        A description for clustering of objects (such as atoms or features).

