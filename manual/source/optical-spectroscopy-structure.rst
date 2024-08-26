.. _Optical-Spectroscopy-Structure-Fairmat:

====================
Optical spectroscopy
====================

.. index::
   OpticalSpec1
   Ellipsometry1
   Raman1
   DispersiveMaterial1

.. _OpticalSpec1:

Optical Spectroscopy
####################




Application Definitions
-----------------------

We created one application definition:

    :ref:`NXoptical_spectroscopy`:
       A general application definition for optical spectroscopy measurements. This includes specifically:
         photoluminescence
         transmission spectroscopy
         reflection spectroscopy
         and general spectroscopy experiments

   General spectroscopy experiments refer to experiments of the type photon-in photon-out. A detector is required to measure the "photon-out"-signal.
   For Ellipsomertry and Raman spectroscopy are specific application definitions listed below.




.. _Ellipsometry1:

Ellipsometry
############

Ellipsometry is an optical characterization method to describe optical properties of interfaces and thickness of films. The measurements are based on determining how the polarization state of light changes upon transmission and reflection. Interpretation is based on Fresnel equations and numerical models of the optical properties of the materials.

This application definition is an extension of :ref:`NXoptical_spectroscopy`. It provide a minimum set of description elements allowing for a reproducible recording of ellipsometry measurements. 


Application Definitions
-----------------------

We created one application definition:

    :ref:`NXellipsometry`:
       A general application definition for ellipsometry measurements, including complex systems up to variable angle spectroscopic ellipsometry. 


.. _Raman1:

Raman spectroscopy
##################

Raman spectroscopy is an optical characterization method by measuring elastic light scattering. In this way phonon characteristics are measured for a extreme broad range of samples: gasses, liquids, solids, glasses, crystals. 

The application definition provides an extension of :ref:`NXoptical_spectroscopy` to cover required or relevant data from Raman scattering experiments.


Application Definitions
-----------------------

We created one application definition:

    :ref:`NXraman`:
       A general application definition for Raman measurements.




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
       This describes a tabular dispersion where the dielectric function is an array versus wavelength or energy.

Formula Grammar
---------------

Below you find a grammar to which the formula should adhere and which can be used to parse and
evaluate the dispersion function. The terms ``single_param_name`` and ``param_name`` should be
filled with the respective single and repeated params from the stored data.

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
       
