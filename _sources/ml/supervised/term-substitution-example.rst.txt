Term substitution example
-------------------------

Given a model template:

.. math::

  w_1 x_1 + \frac{11 + w_2 6x_2^2}{4\sqrt{x_3}}

It has to be transformed in such a way that :math:`w_2` coeficient
is outside of the residual part of its term:

.. math::

  \frac{11 + w_2 6x_2^2}{4\sqrt{x_3}}

  \frac{11}{4\sqrt{x_3}} + \frac{w_2 6x_2^2}{4\sqrt{x_3}}

  \frac{11}{4\sqrt{x_3}} + w_2 \frac{6x_2^2}{4\sqrt{x_3}}

Swap the terms:

.. math::

  w_2 \frac{6x_2^2}{4\sqrt{x_3}} + \frac{11}{4\sqrt{x_3}}

The term with a static coeficient should be transformed to be
a product:

.. math::

  w_2 \frac{6x_2^2}{4\sqrt{x_3}} + \frac{11}{4}\frac{1}{\sqrt{x_3}}

Replace all features that are not first order ones with transient computed
features. Replace all static coeficients with static coefficient aliases.

.. math::

  w_2 x_{2'} + w_{3'}x_{3'}

, where:

.. math::

  x_{2'} = \frac{6x_2^2}{4\sqrt{x_3}}

  x_{3'} = \frac{1}{\sqrt{x_3}}

  w_{3'} = \frac{11}{4}

Static coefficients need to remain unchanged during model training.

Given an example where:

.. math::

  x_1 = 1

  x_2 = 2

  x_3 = 2

The enriched example would look as follows:

.. math::

  x_1 = 1

  x_{2'} = \frac{6}{\sqrt{8}}

  x_{3'} = \frac{1}{\sqrt{8}}