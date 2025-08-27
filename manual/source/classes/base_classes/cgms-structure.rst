.. _BC-Cgms-Structure:

=========================
Geometry & Microstructure
=========================

.. index::
   BC-Cgms-Introduction
   BC-Cgms-Introduction-Physics
   BC-Cgms-Introduction-Base-Classes
   BC-Cgms-Introduction-IcmeMsModels
   
.. literalinclude:: cube_example.txt
    :tab-width: 4
    :linenos:
    :language: text
   

.. _BC-Cgms-Introduction:

Introduction
############

The computational-geometry/microstructure-modeling-based part of the proposal
has the following aims:

To contribute to efforts on standardizing a controlled
vocabulary, definitions for these terms, and relations between the terms, for
computational-geometry-based descriptions of the structure of materials and
atomic configurations used when characterizing materials in experiments
and computer simulations.

As far as NeXus is concerned, this proposed set of simple geometric primitives
and shapes offer a complementary alternative to the current set of base classes in
NeXus for constructive solid geometry such as :ref:`NXcsg`, :ref:`NXoff_geometry`, 
or :ref:`NXquadric` to name but a few.

.. _BC-Cgms-Introduction-Physics:

Physics background
##################
Microstructural features or crystal defects are spatial arrangements of atoms.
Given their specific atomic arrangement and composition, such features have
specific constraints on the degrees of freedom how atoms can arrange. This causes
these defects to have specific properties.
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

Defining crystal defects is a question of how to coarse-grain a given spatiotemporal
set of atoms, each having a nuclide type and position/trajectory. Different mathematical/geometrical
methods exists to coarse-grain and thus determine how a point, a line, a surface, or
a volumetric defect can be described and be spatiotemporally constrained through
a geometrical model with defined geometric primitives and associated (materials)
properties at a coarser-scale.

The key motivation to such coarse-graining is to reduce the complexity of the
description. On the one hand to support visualization and scientific analyses - not only
of crystal defect arrangements. On the other hand it is the hope that using descriptors
at a coarser level, i.e. nanometre, micrometre, and larger, it is still possible
to find sufficiently accurate and precise descriptors that avoid one having to account
for the dynamics of each atom to predict or understand the properties of defects
and their dynamics.

Nevertheless, experience has shown that computational-geometry-based descriptions
when combined with hierarchical clustering/labeling methods, applied on set of
atoms and features turn out to yield useful descriptors. Examples include point,
line, surface defects, such as vacancies, solute cluster, dislocations,
disconnections, interfaces to name but a few.

.. _BC-Cgms-Introduction-Base-Classes:

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

    :ref:`NXorientation_set`:
        A set of parameters to describe the relative orientation of members of a set of features/objects.

    :ref:`NXslip_system_set`:
        Metadata for a set of slip systems in a given crystal structure.

    :ref:`NXms_feature_set`:
        Generic base class to describe any nested set of features
        of a microstructure at the continuum-, micron-, nano-scale, or
        to represent a topology of molecules and atoms.

    :ref:`NXms_snapshot`:
        A container to describe the state of microstructural features
        at a given point in time.

    :ref:`NXms_snapshot_set`:
        The corresponding class to hold a set of :ref:`NXms_snapshot` objects.

    :ref:`NXchemical_composition`:
        (Chemical) composition of a sample or a set of things.

Finally, the following base classes allow data processing software to document its input
parameters and to summarize its performance statistics:

    :ref:`NXprogram`:
        A named and version of a program of library/component.

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

.. _BC-Cgms-Introduction-IcmeMsModels:

Application definitions for ICME models
#######################################

It is important to embrace the large research community of materials engineers
as they are frequent users of electron microscopy and atom probe microscopy.
In this community frequently ICME (Integrated Computational Materials Engineering)
microstructure models are used. These models are derived from a design strategy
and workflow whereby physics-based modelling of microstructure evolution, typically
at the mesoscopic scale, is used to understand the relations between
the microstructure and technological relevant descriptors for the properties
of materials.

The following application definitions are proposed to support discussion on
how materials engineering-specific data models connect to or can be mapped on
concepts which are equally modellable with NeXus:

    :ref:`NXms`:
        An application definition for arbitrary spatiotemporally resolved simulations.

    :ref:`NXms_feature_set`:
        Set of topological/spatial features in materials build from other features.       

    :ref:`NXms_score_config`:
        A specific example of how :ref:`NXapm_paraprobe_config_ranger` can be
        specialized for documenting the configuration of a computer simulation
        with the static recrystallization cellular automata model SCORE.

    :ref:`NXms_score_results`:
        A specific example of how :ref:`NXms` can be specialized for documenting
        results of computer simulations with the static recrystallization
        cellular automata model SCORE.