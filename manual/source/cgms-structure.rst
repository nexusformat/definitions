.. _CGMSFeatures-Structure:

=========================
Geometry & microstructure
=========================

.. index::
   IntroductionCGMS
   PhysicsCGMS
   CGMSNewAppDef
   CGMSNewBC
.. CGMSNewCommonBC


.. _IntroductionCGMS:

Introduction
##############

The computational-geometry/microstructure-modeling-based part of the proposal
has the following aims:

First, we would like to contribute to efforts on standardizing a controlled
vocabulary, definitions for these terms, and relations between the terms, for
computational-geometry-based descriptions of the microstructure of materials
and atomic configurations used when characterizing materials in experiments
and computer simulations.

As far as NeXus is concerned, the here proposed distinct sets of simple
geometric primitives and shapes offer a complementary alternative to the
already existent base classes in NeXus for constructive solid geometry
such as :ref:`NXcsg`, :ref:`NXoff_geometry`, or :ref:`NXquadric` to name a few.

Second, we would like to explore with this proposal how we can harmonize terms
frequently used by materials scientists in the condensed-matter physics with the
NOMAD MetaInfo description.

Third, the proposal should yield a substantiated set of arguments and suggestions
how descriptors for the structure and atomic architecture of materials can be
harmonize. With this we especially would like to reach out and intensify the
cooperation between the materials-science-related consortia of the German
National Research Infrastructure, specifically, FAIRmat, NFDI-MatWerk, NFDI4Ing,
and NFDI4Chem

.. The proposal reaches out to our colleagues in the materials engineering-based
.. consortia to document that there is value in discussing about controlled vocabulary.

.. _PhysicsCGMS:

Physics background
###################
Microstructural features or crystal defects are spatial arrangements of atoms.
Given their specific atomic arrangement and composition, such features have
specific constraints on the degrees of freedom how atoms can arrange. This causes
that these defects have specific properties.
Provided well-defined coarse-graining procedures are used and regions-of-interest
and/or regions-of-applicability are defined, microstructural features are often
characterized and modelled to have associated thermodynamic descriptors.

Another motivation for the proposal was the observation that frequently the design
of file formats for simulation software in the computational materials science especially
those tools at the interface between condensed-matter physics and materials engineering
are frequently reimplementing the wheel (at least partly) when it comes to decide how to store
e.g. atom and feature positions or shape of regions-of-interest, grids, crystals,
grains, precipitates, and dislocations.

Maybe this is a historical burden given the large set of technical terms and jargon
in place, which then motivated pragmatic solutions that resulted in many research groups
have developed similar formats using similar descriptions.

We see this work on base classes and application definitions not primarily an
effort to improve and extend NeXus for now. Rather this part of the proposal
is an effort to support activities in materials science to work towards
common terminology and using controlled vocabularies more frequently.
These are the foundation for more sophisticated thoughts about practically
useful ontologies.

Defining crystal defects is a question of how to coarse-grain a given spatio-
temporal set of atoms, each having a nuclid type and position/trajectory.
In most cases, such a coarse-graining is an ill-posed task because different
mathematical/geometrical methods exists how a point, a line, a surface, or a volumetric defect
can be described and be spatio-temporally constrained through a geometrical model
with defined geometric primitives and associated coarser-scale properties of the defect.

The key motivation to such coarse-graining is to reduce the complexity of the
description. On the one hand to support visualization and scientific analyses - not only
of crystal defect arrangements - and on the other hand it is the hope that using descriptors
at a coarser level, i.e. nanometer, micrometer, and larger, still sufficiently
accurate and precise descriptors can be found without having to dynamics of each
atom to predict or understand the properties of defects and their dynamics.

Nevertheless, experience has shown that computational-geometry-based descriptions
when combined with hierarchical clustering/labeling methods, applied on the set of
atoms, turn out to yield useful descriptors. Examples include point, line, surface defects,
such as vacancies, solute cluster, dislocations, disconnections, interfaces to name but a few.

.. _CGMSNewAppDef:

.. New Application Definitions
.. ############################

.. Work on handshaking between EPICS-controlled experiments and NeXus resulted
.. in one application definition for temperature dependent IV curve measurements.

..  :ref:`NXiv_temp`:
..      Application definition for temperature dependent IV curve measurements.

.. _CGMSNewBC:

New Base Classes
#################

We propose the following base classes, starting with a set of descriptors
for frequently used shapes and geometric primitives:

    :ref:`NXcg_sphere_set`:
        A description for a set of possibly dissimilar spheres.

    :ref:`NXcg_ellipsoid_set`:
        A description for a set of possibly dissimilar rotated ellipsoids.

    :ref:`NXcg_cylinder_set`:
        A description for a set of possibly dissimilar rotated cylinders.

    :ref:`NXcg_point_set`:
        A collection of points with labels or mark data.

    :ref:`NXcg_polyline_set`:
        A collection of lines and linearized segments.

    :ref:`NXcg_triangle_set`:
        A collection (or soup) of triangles.

    :ref:`NXcg_parallelogram_set`:
        A collection of possibly dissimilar parallelograms.

    :ref:`NXcg_triangulated_surface_mesh`:
        A mesh of triangles.

    :ref:`NXcg_polygon_set`:
        A collection (or soup) of polygons.

    :ref:`NXcg_polyhedron_set`:
        A collection (or soup) of polyhedra.

    :ref:`NXcg_roi_set`:
        A container to host a number of different type of primitives.

    :ref:`NXcg_tetrahedron_set`:
        A collection (or soup) of tetrahedra.

    :ref:`NXcg_hexahedron_set`:
        A collection (or soup) of hexahedra with capabilities to represent
        also simpler (bounding) boxes for e.g. binary trees.


These base classes make use of new base classes which describe data structures:

    :ref:`NXcg_face_list_data_structure`:
        In essence, the usual way how polygon/polyhedra data are reported:
        Via a list of vertices and faces with identifier and properties.

    :ref:`NXcg_half_edge_data_structure`:
        A half-edge data structure is a useful complementary descriptor for
        polygon/polyhedra which enables topological analyses and traversal
        of the graph how polygons and polyhedra can be described.

    :ref:`NXcg_unit_normal_set`:
        As an additional structuring element especially for meshes well-documented
        normal information is crucial for distance computations

    :ref:`NXcg_geodesic_mesh`:
        Geodesic meshes are useful for all applications when meshing the surface
        of a sphere.

    :ref:`NXcg_alpha_shape`:
        Alpha shapes and alpha wrappings, specifically the special case of the
        convex hull, are frequently used geometrical models for describing
        a boundary or edge to a set of geometric primitives.


Furthermore, we propose a few base classes for operations when working with
discretized representations of material (area or volume) which can be useful
not only for stencil-based methods:

    :ref:`NXcg_grid`:
        A grid of cells.

    :ref:`NXcg_isocontour`:
        A description for isocontour descriptions.

    :ref:`NXcg_marching_cubes`:
        An approach to store metadata of a specific implementation of
        the Marching Cubes algorithm, whose sensitivity to specific topological
        configurations is known to result in different triangle soups.

    :ref:`NXdelocalization`:
        An approach to document procedures in which a scalar field
        is smoothened in a controlled manner.

Assuming that these base classes can serve as building blocks, we would like
to test with the proposal also how these base classes can be applied in base
classes for specific types of microstructural features and/or utility classes
to hold metadata for these features:

    :ref:`NXclustering`:
        A description for clustering of objects (such as atoms or features).

    :ref:`NXatom_set`:
        A set of atoms.

    :ref:`NXorientation_set`:
        A set of rotations to describe the relative orientation of
        of members of a set of features/objects.

    :ref:`NXslip_system_set`:
        Metadata to a set of slip system/slip system family for
        a given crystal structure.

..    :ref:`NXms_point_defect_set`:
..        Metadata to a set of point defects.

..     :ref:`NXms_dislocation_set`:
..        Metadata of a set of dislocation/disconnection (line) defects.

..    :ref:`NXms_interface_set`:
..        Metadata to a set of interfaces between crystals.

    :ref:`NXms_crystal_set`:
        A set of crystals, for e.g. a polycrystal, phases, 
        grains, precipitates.

    :ref:`NXms_snapshot`:
        A container to describe the state of microstructural features
        at a given point in time.

    :ref:`NXms_snapshot_set`:
        The corresponding class to hold a set of :ref:`NXms_snapshot` objects.

Furthermore, we found that it can be useful to have a set of base classes with
which software documents state and gives a summary for users about the performance
and elapsed time measured while processing data. These utility classes include:

    :ref:`NXcs_filter_boolean_mask`:
        A boolean mask.

    :ref:`NXcs_prng`:
        Metadata of a pseudo-random number generator (PRNG) algorithm.

    :ref:`NXcs_profiling`:
        A structuring group holding a set of :ref:`NXcs_profiling_event` instances.

    :ref:`NXcs_profiling_event`:
        Profiling/benchmark data to an event of
        tracking an algorithm/computational step.

    :ref:`NXcs_computer`:
        Metadata of a computer.

    :ref:`NXcs_cpu`:
        Metadata of a central processing unit.

    :ref:`NXcs_gpu`:
        Metadata of a graphical processing unit / accelerator.

    :ref:`NXcs_mm_sys`:
        Metadata of the (main) memory (sub-)system.

    :ref:`NXcs_io_sys`:
        Metadata of the input/output system.

    :ref:`NXcs_io_obj`:
        Metadata of a component storing data of an :ref:`NXcs_io_sys` instance.


.. _CGMSNewCommonBC:
.. New Common Base Classes
.. #######################

