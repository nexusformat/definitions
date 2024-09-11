.. _CgmsFeatures-Structure:

============================
Geometry and microstructures
============================

.. index::
   IntroductionCgms
   PhysicsCgms
   CgmsAppDef
   CgmsBC


.. _IntroductionCgms:

Introduction
############

The computational-geometry/microstructure-modeling-based part of the proposal
has the following aims:

First, to contribute to efforts on standardizing a controlled vocabulary, definitions for terms,
and relations between terms, for computational-geometry-based descriptions of the structure of
materials and atomic configurations used when characterizing materials in experiments
and computer simulations.

As far as NeXus is concerned, this proposed set of geometric primitives offer
a complementary alternative to the current set of base classes in NeXus for
constructive solid geometry (CSG) such as :ref:`NXcsg`, :ref:`NXoff_geometry`, or :ref:`NXquadric`.

Second, to explore how terms which are frequently used by materials scientists in the field of
condensed-matter physics can be harmonized with definitions and terms offer by the NOMAD MetaInfo
description. NOMAD MetaInfo is the data schema of the NOMAD research data management system.

Third, to yield a substantiated set of arguments and suggestions how descriptors for the structure
and the atomic architecture of materials can be harmonized. Especially this proposal reaches out to
other materials-science-related projects and consortia including the activities in the German NFDI
FAIRmat, NFDI-MatWerk, NFDI4Ing, NFDI4Chem, NFDI4Cat, MaRDI, and DAPHNE.

.. _PhysicsCgms:

Physics background
##################
Microstructural features or crystal defects are spatial arrangements of atoms.
Given their specific atomic arrangement and composition, such features have
specific constraints on the degrees of freedom. This causes these defects to have specific
properties (thermodynamic observables/descriptors). Provided well-defined coarse-graining procedures
are used and regions-of-interest and/or regions-of-applicability are defined, microstructural
features are often characterized and modelled to have associated thermodynamic descriptors.

Another motivation for the proposal was the observation that frequently the design
of file formats for simulation software in the computational materials science especially
at the interface between condensed-matter physics and materials engineering are frequently
reimplementing the wheel when it comes to making decision how to store e.g. atom and feature positions
or how to document the shape of regions-of-interest, grids, crystals, grains, precipitates, and dislocations.
This generates a diversity of file formats and data schemas which hampers semantic interpretation
and interoperability.

Maybe this is a historical burden given the large set of technical terms in place which then
motivated pragmatic solutions that have resulted in many research groups having developed
similar formats using similar descriptions.

Defining crystal defects is a question of how to coarse-grain a given spatiotemporal set of atoms,
each having a nuclide type and position/trajectory. Different mathematical/geometrical methods exists
to determine how a point, a line, a surface, or a volumetric defect can be described and be spatiotemporally constrained through a geometrical model
with defined primitives and associated observables.

The key motivation to such coarse-graining is to reduce the complexity of the description.
On the one hand to support visualization and scientific analyses - not only of crystal defect arrangements.
On the other hand it is the hope that using descriptors at a coarser level, i.e. nanometer, micrometer, and larger,
are still sufficiently accurate and precise to yield descriptors which avoid that one has
to account for the dynamics of each atom to predict or understand the properties
of defects and their dynamics.

Experience has shown that computational-geometry-based descriptions
when combined with hierarchical clustering/labeling methods, applied on sets of
atoms and features turn out to yield useful descriptors. Examples include point,
line, surface defects, such as vacancies, solute cluster, dislocations,
disconnections, interfaces to name but a few.

.. _CgmsBC:

Base Classes
############

The following base classes are defined to incentivize the use of NeXus for using
computational-geometry-based descriptions. In what follows, base classes
for frequently used shapes and geometric primitives are proposed:

    :ref:`NXcg_primitive_set`:
        A base class to inherit from when defining base classes for specific primitives such as these:

    :ref:`NXcg_sphere_set`:
        A base class for a set of possibly dissimilar spheres.

    :ref:`NXcg_ellipsoid_set`:
        A base class for a set of possibly dissimilar rotated ellipsoids.

    :ref:`NXcg_cylinder_set`:
        A base class for a set of possibly dissimilar rotated cylinders.

    :ref:`NXcg_point_set`:
        A base class for a collection of points with labels or mark data.

    :ref:`NXcg_polyline_set`:
        A base class for a collection of lines and linearized segments.

    :ref:`NXcg_triangle_set`:
        A base class for a collection (or soup) of triangles.

    :ref:`NXcg_parallelogram_set`:
        A base class for a collection of possibly dissimilar parallelograms.

    :ref:`NXcg_triangulated_surface_mesh`:
        A base class for a collection and/or mesh of triangles.

    :ref:`NXcg_polygon_set`:
        A base class for a collection (or soup) of polygons.

    :ref:`NXcg_polyhedron_set`:
        A base class for a collection (or soup) of polyhedra.

    :ref:`NXcg_roi_set`:
        A container to host a number of different types of primitives.

    :ref:`NXcg_tetrahedron_set`:
        A base class for a collection (or soup) of tetrahedra.

    :ref:`NXcg_hexahedron_set`:
        A base class for a collection (or soup) of hexahedra to represent
        e.g. simpler (bounding) boxes for e.g. binary trees.

These base classes make use of base classes which describe data structures:

    :ref:`NXcg_face_list_data_structure`:
        A base class to store the usual way how polygon/polyhedra data are reported:
        Via a list of vertices and faces with identifiers and properties.

    :ref:`NXcg_half_edge_data_structure`:
        A base class for more advanced but more efficiently traversable data structure:
        A half-edge data structure is a useful complementary descriptor for
        polygon/polyhedra which enables topological analyses and traversal of half-edges
        about a topology of primitives.

    :ref:`NXcg_unit_normal_set`:
        A base class for storing primitive unit normal vectors.

    :ref:`NXcg_geodesic_mesh`:
        Geodesic meshes are useful for all applications when meshing the surface of a sphere
        with many applications in the analyses of diffraction data.

    :ref:`NXcg_alpha_complex`:
        Alpha shapes and alpha wrappings, specifically the special case of the
        convex hull, are frequently used geometrical models for describing
        a boundary or edge to a set of geometric primitives.

Furthermore, a few base classes are defined for documenting the working with
discretized representations of material (area or volume) which can be useful
not only for stencil-based methods:

    :ref:`NXcg_grid`:
        A base class for a grid of cells discretizing e.g. a computational domain
        or computation with models using representative volume elements (RVEs).

    :ref:`NXisocontour`:
        A base class for isocontour descriptions.

    :ref:`NXcg_marching_cubes`:
        A base class to store metadata of a specific implementation of
        the Marching Cubes algorithm, whose sensitivity to specific topological
        configurations is known to result in different triangle soups.
        This is relevant e.g. for computations of isocontours.

    :ref:`NXdelocalization`:
        A base class to document procedures whereby a scalar field
        is smoothened in a controlled manner (typically using kernel methods).

    :ref:`NXsimilarity_grouping`:
        A base class to describe clustering of objects (such as atoms or features).

    :ref:`NXrotation_set`:
        A base class to describe the relative orientation or rotation members
        of a set of features/objects.

    :ref:`NXchemical_composition`:
        A base class to document (chemical) composition of a sample or a set of things.

Finally, the following base classes allow data processing software to document its
input parameters and to summarize its performance statistics:

    :ref:`NXprogram`:
        A base class for a specifically named and versioned program or library/component.

    :ref:`NXcs_filter_boolean_mask`:
        A base class for a boolean mask.

    :ref:`NXcs_prng`:
        A base class for settings of a pseudo-random number generator (PRNG) algorithm.

    :ref:`NXcs_profiling`:
        A base class for holding a set of :ref:`NXcs_profiling_event` instances.

    :ref:`NXcs_profiling_event`:
        A base class for documenting profiling/benchmark for an algorithm or computational step.

    :ref:`NXcs_computer`:
        Base class for describing a computer and its components.
