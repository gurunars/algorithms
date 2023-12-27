Derivation
==========

Meaning
-------

The rate of change of a function with respect to a variable.

.. note::

    This document follows `Lagrange's notation <https://en.wikipedia.org/wiki/Notation_for_differentiation#Lagrange's_notation>`_.

General formula
---------------

.. math::

    f'(x) = \lim_{\Delta{x} \to 0} \frac{f(x+\Delta{x}) - f(x)}{\Delta{x}}

Examples
--------

1st degree polynomyal
^^^^^^^^^^^^^^^^^^^^^

Given:

.. math::

    f(x) = 2x - 3

Then:

.. math::

    f'(x) = \lim_{\Delta{x} \to 0} \frac{(2(x+\Delta{x}) - 3) - (2x - 3)}{\Delta{x}}

    f'(x) = \lim_{\Delta{x} \to 0} \frac{2x + 2\Delta{x} - 3 - 2x + 3}{\Delta{x}}

    f'(x) = \lim_{\Delta{x} \to 0} \frac{2\Delta{x}}{\Delta{x}}

    f'(x) = \lim_{\Delta{x} \to 0} 2

And after replacing :math:`\Delta{x}` with ``0``

.. math::

    f'(x) = 2

2nd degree polynomyal
^^^^^^^^^^^^^^^^^^^^^

Given:

.. math::

    f(x) = 4x^2 + 3x + 11

.. math::

    f'(x) = \lim_{\Delta{x} \to 0} \frac{(4(x+\Delta{x})^2 + 3(x+\Delta{x}) + 11) - (4x^2 + 3x + 11)}{\Delta{x}}

    f'(x) = \lim_{\Delta{x} \to 0} \frac{4(x^2 + 2x\Delta{x} + \Delta{x}^2) + 3x + 3\Delta{x} + 11 - 4x^2 - 3x - 11}{\Delta{x}}

    f'(x) = \lim_{\Delta{x} \to 0} \frac{4x^2 + 8x\Delta{x} + 4\Delta{x}^2 + 3x + 3\Delta{x} + 11 - 4x^2 - 3x - 11}{\Delta{x}}

    f'(x) = \lim_{\Delta{x} \to 0} \frac{8x\Delta{x} + 4\Delta{x}^2 + 3\Delta{x}}{\Delta{x}}

    f'(x) = \lim_{\Delta{x} \to 0} \frac{\Delta{x}(8x + 4\Delta{x} + 3)}{\Delta{x}}

    f'(x) = \lim_{\Delta{x} \to 0} 8x + 4\Delta{x} + 3

And after replacing :math:`\Delta{x}` with ``0``

.. math::

    f'(x) = 8x + 3

Total derivative
----------------

.. math::

    f'(x_1, \ldots, x_n) = \sum_{i=1}^{n} f_{x_i}'(x_1, \ldots, x_n)

Partial derivative
------------------

An expression:

.. math::

    f_{x_i}'

Means that only :math:`x_i` is replaced with :math:`x_i + \Delta{x_i}` during derivation.

Example
^^^^^^^

Given:

.. math::

    f(x,y,z) = x^2 + 3y^3 - 2z

Partial derivative for :math:`x` in a general sense is:

.. math::

    f_{x}'(x,y,z) = \lim_{\Delta{x} \to 0}\frac{f(x+\Delta{x},y,z) - f(x,y,z)}{\Delta{x}}

    f_{x}'(x,y,z) = \lim_{\Delta{x} \to 0}\frac{((x+\Delta{x})^2 + 3y^3 - 2z) - (x^2 + 3y^3 - 2z)}{\Delta{x}}

    f_{x}'(x,y,z) = 2x