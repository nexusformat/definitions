.. _Optical-Spectroscopy-Structure:

====================
Optical Spectroscopy
====================

.. index::
   Ellipsometry
   Raman
   DispersiveMaterial


.. _Ellipsometry:

Ellipsometry
############

Ellipsometry is an optical characterization method to describe optical properties of interfaces and thickness of films.
The measurements are based on determining how the polarization state of light changes upon transmission and reflection.
Interpretation is based on Fresnel equations and numerical models of the optical properties of the materials.

In the application definition we provide a minimum set of description elements allowing for a reproducible recording of ellipsometry measurements. 

.. _Raman:

Raman
############

Raman spectroscopy is a characterization method to analyze vibrational properties for liquids, gases or solids. 
The measurements is based on the inelastic light scattering due to the materials vibrations.
Interpretation can be done based on peaks, which represent the phonon properties (intensity, center, width).

The application provides a minimum set of description elements, which are necessary to understand for Raman spectroscopy measurements.



Application Definitions
-----------------------

    :ref:`NXoptical_spectroscopy`:
       A generic application definition for optial spectorscopy measurements. This including specifically ellipsometry and Raman spectroscopy measurements, but as well other techniques such as photoluminescence, transmission, reflection measurements. The requirements are: (i) an incident photon beam, (ii) a detector to measure scattered/emitted photons and (iii) a sample.

    :ref:`NXellipsometry`:
       An application definition for ellipsometry measurements, including complex systems up to variable angle spectroscopic ellipsometry.

    :ref:`NXraman`:
       An application definition for Raman spectroscopy measurements.


Base Classes
------------

This is the set of base classes for describing an optical experiment.

    :ref:`NXbeam_device`
       Beam devices are used to relate a beam, which has always at least one origin
       and at least one destination. 
       
       By referencing the beam devices with each other, a beam path can be
       constructed. This can be used for vizualization or beam propery modeling
       along the beam path.

    :ref:`NXbeam`
      Beam properties such as intensity, polarization, wavelength or direction.

    :ref:`NXdetector`
      A detector for signal detection.

    :ref:`NXsource`
      A light source such as laser, lamp or LED.

    :ref:`NXmonochromator`
      A monochromator is often used to energetically disperse the scattered or emitted light.

    :ref:`NXlens_opt`
       Description of an optical lens.
       
    :ref:`NXwaveplate`
       A waveplate or retarder.

    :ref:`NXsensor`
       Specify external parameters that have influenced the sample such as
       varied parameters e.g. temperature, pressure, pH value, beam intensity, etc.



.. _DispersiveMaterial:

Dispersive Material
###################

A dispersive material is a description for the optical dispersion of materials.
This description may be used to store optical model data from an ellipsometric analysis 
(or any other technique) or to build a database of optical constants for optical properties of materials.

Application Definition
----------------------

    :ref:`NXdispersive_material`:
       An application definition to describe the dispersive properties of a material.
       The material may be isotropic, uniaxial or biaxial. Hence, it may contain up
       to three dispersive functions or tables.



Base Classes
------------

There is a set of base classes for describing a dispersion.

    :ref:`NXdispersion`
       This is an umbrella base class for a group of dispersion functions to describe the material.
       For a simple dispersion it may contain only on NXdispersion_function or NXdispersion_table entry.
       If it contains multiple entries the actual dispersion is the sum of all dispersion functions and tables.
       This allows for, e.g. splitting real and imaginary parts and describing them seperately or
       adding a dielectric background (e.g. Sellmeier model) to an oscillator model (e.g. Lorentz).
              
    :ref:`NXdispersion_function`
       This dispersion is described by a function and its single and repeated parameter values.
       It follows a formula of the form ``eps = eps_inf + sum[A * lambda ** 2 / (lambda ** 2 - B ** 2)]`` 
       (Sellmeier formula). See the formula grammar below for an ebnf grammar for this form.

    :ref:`NXdispersion_single_parameter`
       This denotes a parameter which is used outside the summed part of a dispersion function,
       e.g. ``eps_inf`` in the formula example above.

    :ref:`NXdispersion_repeated_parameter`
       This denotes arrays of repeated parameters which are used to build a sum of parameter values, e.g.
       ``A`` and ``B`` are repeated parameters in the formula above.
       
    :ref:`NXdispersion_table`
       This describes a tabular dispersion where the permittivity is an array versus wavelength or energy.

Formula Grammar
---------------

Below you find a grammar to which the formula should adhere and which can be used to parse and
evaluate the dispersion function. The terms ``single_param_name`` and ``param_name`` should be
filled with the respective single and repeated params from the stored data.
The grammer is written in the `EBNF <https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form>`_ dialect
of `Lark <https://github.com/lark-parser/lark>`_, which is a parsing toolkit for python.
It is easily translatable to general EBNF and other parser generator dialects.
`Here <https://github.com/PyEllips/formula-dispersion>`_ is a reference implementation in Rust/Python with a
`grammar <https://github.com/PyEllips/formula-dispersion/blob/main/src/formula_parser.lalrpop>`_
written in `lalrpop <https://github.com/lalrpop/lalrpop>`_.

.. code-block::

   ?assignment: "eps" "=" kkr_expression -> eps
             | "n" "=" kkr_expression -> n

   ?kkr_expression: expression
                  | "<kkr>" "+" "1j" "*" term -> kkr_term

   ?expression: term
               | expression "+" term -> add
               | expression "-" term -> sub

   ?term: factor
         | term "*" factor -> mul
         | term "/" factor -> div

   ?factor: power
         | power "**" power -> power


   ?power: "(" expression ")"
         | FUNC "(" expression ")" -> func
         | "sum" "[" repeated_expression "]" -> sum_expr
         | NAME -> single_param_name
         | SIGNED_NUMBER -> number
         | BUILTIN -> builtin

   ?repeated_expression: repeated_term
                     | repeated_expression "+" repeated_term -> add
                     | repeated_expression "-" repeated_term -> sub


   ?repeated_term: repeated_factor
                  | repeated_term "*" repeated_factor -> mul
                  | repeated_term "/" repeated_factor -> div

   ?repeated_factor: repeated_power
                     | repeated_power "**" repeated_power -> power

   ?repeated_power: "(" repeated_expression ")"
                  | FUNC "(" repeated_expression ")" -> func
                  | SIGNED_NUMBER -> number
                  | NAME -> param_name
                  | BUILTIN -> builtin

   FUNC.1: "sin" | "cos" | "tan" | "sqrt" | "dawsn" | "ln" | "log" | "heaviside" 
   BUILTIN.1: "1j" | "pi" | "eps_0" | "hbar" | "h" | "c" 

   %import common.CNAME -> NAME
   %import common.SIGNED_NUMBER
   %import common.WS_INLINE

   %ignore WS_INLINE
       
