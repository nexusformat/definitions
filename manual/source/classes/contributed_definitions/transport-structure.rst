.. _CC-Transport-Structure:

===================
Transport Phenomena
===================

.. index::
   CC-Transport-Introduction
   CC-Transport-Definitions


.. _CC-Transport-Introduction:

Introduction
##############

Many experiments in condensed-matter physics and materials engineering belong to the category
of measurements of transparent phenomena. A possible example of such experiments are temperature-dependent
current-voltage (IV) curve measurements (or JV for engineers) measurements. In this case, electrical charge is transported
and the temperature-dependent current response as a function of applied voltage is recorded.


.. _CC-Transport-Definitions:

Application Definitions
#######################

Below is an example for such an application definition for an experiment. This application definition has exemplar parts
which show how such an experiment can be controlled with the `EPICS system <https://epics-controls.org/about-epics/>`_:

:ref:`NXsensor_scan`
    Application definition for a generic scan using sensors.

:ref:`NXiv_temp`
    Application definition for temperature-dependent current-voltage (IV) curve measurements.
