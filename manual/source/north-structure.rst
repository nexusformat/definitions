.. _North-Structure1:

======================
Nomad Remote Tools Hub
======================


.. index::
   IntroductionApmParaprobe1
   WhatHasBeenAchieved1
   ApmParaprobeAppDef1
   ApmParaprobeNewBC1
   NextStep1


.. _IntroductionApmParaprobe1:

Introduction
##############

NORTH (the NOMAD Oasis Remote Tools Hub) is a NOMAD Oasis service which makes
preconfigured scientific software of different communities available and coupled
to Oasis and accessible via the webbrowser. This part of the proposal documents
examples for specific NeXus-related work to some of the tools and containers
available in NORTH.


apmtools
########

One tool is the paraprobe-toolbox software package in the the apmtools container.
The software is developed by `M. Kühbach et al. <https://arxiv.org/abs/2205.13510>`_.

Here we show how NeXus is used to consistently define application definitions
for scientific software in the field of atom probe. In this community the paraprobe-toolbox is an example of an open-source parallelized
software for analyzing point cloud data, for assessing meshes in 3D continuum
space, and analyzing the effects of parameterization on descriptors
about the microstructure of materials which were studied with atom probe microscopy.

The need for a thorough documentation of the tools in not only the paraprobe-toolbox was motivated by several needs:

First, users of software would like to better understand and also be able to
study themselves which individual parameter and settings for each tool exist
and how configuring these affects their analyses quantitatively.

Second, scientific software like the tools in the paraprobe-toolbox implement a
numerical/algorithmical (computational) workflow whereby data from multiple input sources
(like previous analysis results) are processed and carried through more involved analysis
within several steps inside the tool. The tool then creates output as files.

Individual tools are developed in C/C++ and/or Python. Here, having a possibility
for provenance tracking is useful as it is one component and requirement for
making workflows exactly numerically reproducible and thus to empower scientists
to fullfill better the "R", i.e. reproducibility of daily FAIR research practices.

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


.. _WhatHasBeenAchieved1:

What has been achieved so far?
##############################

This proposal summarizes both of the steps which we worked on between Q3/2022-Q1/2023 to change the interface and
file interaction in all tools of the paraprobe-toolbox to accept exclusively
well-defined configuration files and yield exclusively specific output.

Data and metadata between the tools are exchanged with NeXus/HDF5 files.
Specifically, we created for each tool an application definition (see below)
which details all possible settings and options for the configuration as to
guide users. The config(uration) files are HDF5 files, whose content matches
to the naming conventions of the respective `config` application definition for each tool.
As an example NXapm_paraprobe_config_surfacer specifies how a configuration file
for the paraprobe-surfacer tool should be formatted and which parameter it contains.

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
were achieved with a specific chain of input and
settings using specifically-versioned tools.

We understand that this additional handling of metadata and provenance tracking
may not be at first glance super relevant for scientists or appears to be an
unnecessarily complex feature. There is indeed an additional layer of work which
came with the development and maintenance of this functionality.

However, we are convinced that this is the preferred way of performing software
development and data analyses as it enables users to take advantage of a completely
automated provenance tracking which happens silently in the background.

.. _ApmParaprobeAppDef1:

Application Definitions
#######################

Firstly, we define application definitions for the input side (configuration) of each tool.

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

Secondly, we define application definitions for the output side (results) of each tool.

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

.. _ApmParaprobeNewBC1:

Base Classes
############

We envision that the above-mentioned definitions can be useful not only to take
inspiration for other software tools in the field of atom probe but also to support
a discussion towards a stronger standardization of the vocabulary used.
Therefore, we are happy for your comments and suggestions on this and the related
pages via the hypothesis web annotation service or as your issues posted on GitHub.

We are convinced that the majority of data analyses in atom probe use
an in fact common set of operations and conditions on the input data
even though this might not be immediately evident. In particular this is not
the case for some community built tools with a very specific scope where oftentimes
the algorithms are hardcoded for specific material systems. A typical example is a
reseacher who implements a ranging tool and uses that all the examples are on a
specific material. We are convinced it is better to follow a much more generalized approach.

In this spirit, we propose the following base classes and the above application
definitions as examples how very flexible constraints can be implemented which
restrict which ions in the dataset should be processed or not. We see that these
suggestions complement the proposal on computational geometry base classes:

    :ref:`NXapm_input_reconstruction`:
        A description from which file the reconstructed ion positions are imported.

    :ref:`NXapm_input_ranging`:
        A description from which file the ranging definitions are imported.
        The design of the ranging definitions is, thanks to :ref:`NXion` so
        general that all possible nuclids can be considered, be they observationally stable, 
        be they radioactive or transuranium nuclids.

A detailed inspection of spatial and other type of filters used in atom probe microscopy
data analysis revealed that it is better to define atom probe agnostic, i.e. more
general filters:

    :ref:`NXspatial_filter`:
        A proposal how a point cloud can be spatial filtered in a very specific,
        flexible, yet general manner. This base class takes advantage of
        :ref:`NXcg_ellipsoid_set`, :ref:`NXcg_cylinder_set`, and :ref:`NXcg_hexahedron_set`
        to cater for all of the most commonly used geometric primitives in
        atom probe.

    :ref:`NXsubsampling_filter`:
        A proposal for a filter that can also be used for specifying how entries
        like ions can be filtered via sub-sampling.

    :ref:`NXmatch_filter`:
        A proposal for a filter that can also be used for specifying how entries
        like ions can be filtered based on their type (ion species)
        or hit multiplicity.

In summary, we report with this proposal our experience made in an experimental
project that is about using NeXus for standardizing a set of non-trivial scientific software tools.
During the implementation we learned that for handling computational geometry
and microstructure-related terms many subtilities have to be considered which
makes a controlled vocabulary valuable not only to avoid a reimplementing of the wheel.
