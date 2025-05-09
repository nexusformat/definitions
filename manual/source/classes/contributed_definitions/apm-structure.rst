.. _Contributed-Apm-Structure:

=========================
Atom-probe tomography
=========================

.. index::
   Contributed-Apm-Introduction
   Contributed-Apm-Definitions
   ApmBC
   WhatHasBeenAchieved
   ApmParaprobeAppDef
   ApmParaprobeNewBC
   NextStep


.. _Contributed-Apm-Introduction:

Introduction
##############

:ref:`Application definitions &lt;AppDef-Apm-Definitions&gt;` and :ref:`base classes &lt;BC-Apm-Classes&gt;` to describe atom-probe tomography/microscopy (APT/APM) experiments
are already part of the NeXus standard. In addition, there are several contributed definitions that are currently
under discussion.

.. _ApmAppDef:

Contributed Definitions
######################

Microscopy experiments, not only taking into account those performed on commercial instruments, 
offer the user usually to apply a set of data processing steps. Some of them are frequently applied
on-the-fly. For now these steps are represented in :ref:`NXapm` with specifically named instances of the
:ref:`NXprocess` base class.

Like every research community data processing steps are essential to transform measurements
into knowledge. These processing steps should be documented to enable reproducible research
and learn how pieces of information were connected. In what follows, an example is presented
how an open-source community software can be modified to use descriptions of these computational
steps. The respective research software here is the `paraprobe-toolbox <https://paraprobe-toolbox.readthedocs.io/>`_

.. _Contributed-Apm-Paraprobe:

apmtools
########

One tool is the paraprobe-toolbox software package in the the apmtools container.
The software is developed by `M. Kühbach et al. <https://arxiv.org/abs/2205.13510>`_.

Here we show how NeXus is used to consistently define application definitions for scientific software
in the field of atom probe. In this community the paraprobe-toolbox is an example of an
open-source parallelized software for analyzing point cloud data, for assessing meshes in
3D continuum space, and for studying the effects of parameterization on descriptors
which describe the micro- and nanostructure of materials that are studied with
atom probe microscopy.

The need for a thorough documentation of the tools in not only the paraprobe-toolbox
was motivated by several needs:

First, users of software would like to better understand and also be able to
study for themselves which individual parameters and settings for each tool exist
and how configuring these affects their analyses quantitatively.

Second, scientific software like the tools in the paraprobe-toolbox implement a
numerical/algorithmical (computational) workflow whereby data from multiple input sources
(like previous analysis results) are processed and carried through more involved analysis
within several steps inside the tool. The tool then creates output as files.

Individual tools of paraprobe-toolbox are developed in C/C++ and/or Python.
Provenance tracking is useful as it is one component and requirement for making
workflows exactly numerically reproducible and thereby empower scientists
to fulfill better the "R", i.e. reproducibility of their daily FAIR research practices.

The paraprobe-toolbox is one example of a software which implements a workflow
via a sequence of operations executed within a jupyter notebook
(or Python script respectively). Specifically, individual tools are chained.
Convenience functions are available to create well-defined input/configuration
files for each tool. These config files instruct the tool upon processing.

In this design, each workflow step (with a tool) is in fact a pair (or triple) of
at least two sub-steps: i) the creation of a configuration file, 
ii) the actual analysis using the Python/or C/C++ tools, 
iii) the optional post-processing/visualizing of the results inside the NeXus/HDF5
files generated from each tool run using other software.


.. _WhatHasBeenAchieved:

What has been achieved so far?
##############################

This proposal summarizes work of members of the FAIRmat project, which is part
of the German National Research Data Infrastructure aimed at a change of the paraprobe-toolbox
and its interaction with files for all tools so that only well-defined configuration files
are accepted as input and results end up as specifically formatted output. For this
NeXus application definitions are used.

Data and metadata between the tools are exchanged with NeXus/HDF5 files.
Specifically, we created for each tool an application definition (see below)
which details all possible settings and options for the configuration as to
guide users. The config(uration) files are currently implemented as HDF5 files,
whose content matches to the naming conventions of the respective `config` application
definition for each tool. As an example NXapm_paraprobe_config_surfacer specifies
how a configuration file for the paraprobe-surfacer tool should be formatted
and which parameter it should and/or may contain.

That is each config file uses a controlled vocabulary of terms. Furthermore,
the config files store a SHA256 checksum for each input file.
This implements a full provenance tracking on the input files along the
processing chain/workflow.

As an example, a user may first range their reconstruction and then compute
correlation functions. The config file for the ranging tool stores the files
which hold the reconstructed ion position and ranging definitions.
The ranging tool generates a results file with the ion type labels stored.
This results file is formatted according to the tool-specific `results`
application definition. This results file and the reconstruction is
imported by the spatial statistics tool which again keeps track of all files.

This design makes it possible to rigorously trace which numerical results
were achieved with a specific input and settings using specifically-versioned tools.

We understand that this additional handling of metadata and provenance tracking
may not be at first glance super relevant for scientists or appears to be an
unnecessarily complex feature. There is indeed an additional layer of work which
came with the development and maintenance of this functionality.

However, we are convinced that this is the preferred way of performing software
development and data analyses as it enables users to take advantage of a completely
automated provenance tracking which happens silently in the background.

.. _ApmParaprobeAppDef:

Application Definitions
#######################

Application definitions for the input side (configuration) of each tool were defined.

    :ref:`NXapm_paraprobe_config_transcoder`:
        Configuration of paraprobe-transcoder
        Load POS, ePOS, APSuite APT, RRNG, RNG, and NXapm HDF5 files.

    :ref:`NXapm_paraprobe_config_ranger`:
        Configuration of paraprobe-ranger
        Apply ranging definitions and explore possible molecular ions.

    :ref:`NXapm_paraprobe_config_selector`:
        Configuration of paraprobe-selector
        Defining complex spatial regions-of-interest to filter reconstructed datasets.

    :ref:`NXapm_paraprobe_config_surfacer`:
        Configuration of paraprobe-surfacer
        Create a model for the edge of a point cloud via convex hulls, alpha shapes.

    :ref:`NXapm_paraprobe_config_distancer`:
        Configuration of paraprobe-distancer
        Compute analytical distances between ions to a set of triangles.

    :ref:`NXapm_paraprobe_config_tessellator`:
        Configuration of paraprobe-tessellator
        Compute Voronoi cells for if desired all ions in a dataset.

    :ref:`NXapm_paraprobe_config_nanochem`:
        Configuration of paraprobe-nanochem
        Compute delocalization, iso-surfaces, analyze 3D objects, and composition profiles.

    :ref:`NXapm_paraprobe_config_intersector`:
        Configuration of paraprobe-intersector
        Assess intersections and proximity of 3D triangulated surface meshes in
        continuum space to study the effect the parameterization of surface
        extraction algorithms on the resulting shape, spatial arrangement,
        and colocation of 3D objects via graph-based techniques.

    :ref:`NXapm_paraprobe_config_spatstat`:
        Configuration of paraprobe-spatstat
        Spatial statistics on the entire or selected regions of the reconstructed dataset.

    :ref:`NXapm_paraprobe_config_clusterer`:
        Configuration of paraprobe-clusterer
        Import cluster analysis results of IVAS/APSuite and perform clustering
        analyses in a Python ecosystem.

Application definitions for the output side (results) of each tool were defined.

    :ref:`NXapm_paraprobe_results_transcoder`:
        Results of paraprobe-transcoder
        Store reconstructed positions, ions, and charge states.

    :ref:`NXapm_paraprobe_results_ranger`:
        Results of paraprobe-ranger
        Store applied ranging definitions and combinatorial analyses of all possible iontypes.

    :ref:`NXapm_paraprobe_results_selector`:
        Results of paraprobe-selector
        Store which points are inside or on the boundary of complex spatial regions-of-interest.

    :ref:`NXapm_paraprobe_results_surfacer`:
        Results of paraprobe-surfacer
        Store triangulated surface meshes of models for the edge of a dataset.

    :ref:`NXapm_paraprobe_results_distancer`:
        Results of paraprobe-distancer
        Store analytical distances between ions to a set of triangles.

    :ref:`NXapm_paraprobe_results_tessellator`:
        Results of paraprobe-tessellator
        Store volume of all Voronoi cells about each ion in the dataset.

    :ref:`NXapm_paraprobe_results_nanochem`:
        Results of paraprobe-nanochem
        Store all results of delocalization, isosurface, and interface detection algorithms,
        store all extracted triangulated surface meshes of found microstructural features,
        store composition profiles and corresponding geometric primitives (ROIs).

    :ref:`NXapm_paraprobe_results_intersector`:
        Results of paraprobe-intersector
        Store graph of microstructural features and relations/link identified between them.

    :ref:`NXapm_paraprobe_results_spatstat`:
        Results of paraprobe-spatstat
        Store spatial correlation functions.

    :ref:`NXapm_paraprobe_results_clusterer`:
        Results of paraprobe-clusterer
        Store results of cluster analyses.

.. _ApmParaprobeNewBC:

Base Classes
############

We envision that the above-mentioned definitions can be useful not only to take
inspiration for other software tools in the field of atom probe but also to support
a discussion towards a stronger standardization of the vocabulary used.
Therefore, we are happy for comments and suggestions.

The majority of data analyses in atom probe use a common set of operations and
conditions on the input data even though this might not be immediately evident
or might not have been so explicitly communicated in the literature.
Some tools have a specific scope because of which algorithms are hardcoded
to work for specific material systems. A typical example is a ranging tool
which exploits that all the examples it is used for apply to a specific material
and thus specific iontypes can be hardcoded.

Instead, we are convinced it is better to follow a more generalized approach.
The following base classes and the above application definitions present examples
how one can use NeXus for this.

    :ref:`NXapm_input_reconstruction`:
        A description from which file the reconstructed ion positions are imported.

    :ref:`NXapm_input_ranging`:
        A description from which file the ranging definitions are imported.
        The design of the ranging definitions is, thanks to :ref:`NXion`, so
        general that all possible nuclids can be considered, be they observationally
        stable, be they radioactive or transuranium nuclids.

A detailed inspection of spatial and other type of filters frequently used in
analysis of atom probe data revealed that it is better to define atom-probe-agnostic,
i.e. more general filters:

    :ref:`NXspatial_filter`:
        A proposal how a point cloud can be spatially filtered in a specific yet general manner.
        This base class takes advantage of :ref:`NXcg_ellipsoid_set`, :ref:`NXcg_cylinder_set`,
        and :ref:`NXcg_hexahedron_set` to cater for all of the most commonly used
        geometric primitives in atom probe.

    :ref:`NXsubsampling_filter`:
        A proposal for a filter that can also be used for specifying how entries
        like ions can be filtered via sub-sampling.

    :ref:`NXmatch_filter`:
        A proposal for a filter that can also be used for specifying how entries
        like ions can be filtered based on their type (ion species)
        or hit multiplicity.
