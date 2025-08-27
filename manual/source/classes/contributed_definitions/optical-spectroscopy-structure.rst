.. _Contributed-Opt-Spec-Structure:

========================
Optical Spectroscopy
========================

.. index::
   Contributed-Opt-Spec-Introduction
   Contributed-Apm-Definitions
   Contributed-Opt-Spec-DispersiveMaterial


.. _Contributed-Opt-Spec-Introduction:

Introduction
##############

:ref:`Application definitions &lt;AppDef-Opt-Spec-Definitions&gt;` and :ref:`base classes &lt;BC-Opt-Spec-Classes&gt;` 
to describe optical spectroscopy experiments are already part of the NeXus standard. In addition, there are several 
contributed definitions that are currently under discussion.

.. _Contributed-Opt-Spec-Definitions:

Application Definitions
-----------------------

    :ref:`NX...`:
       text. 


Base Classes
------------

These are new base classes to describe additional, yet to be standardized components of optical spectroscopy experiments.
            
    :ref:`NXbeam_splitter`
       A beam splitter, i.e. a device splitting the light into two or more beams.
       
       Use two or more NXbeam_paths to describe the beam paths after the beam
       splitter. In the dependency chain of the new beam paths, the first elements
       each point to this beam splitter, as this is the previous element.

    :ref:`NXfiber`
       An optical fiber, e.g. glass fiber.
       
    :ref:`NXpolarizer_opt`
       An optical polarizer.

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
       
