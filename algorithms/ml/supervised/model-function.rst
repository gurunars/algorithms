Model function
==============

The function is always a first order polynomial with `j` terms augumented by a **bias** parameter `b`:

.. math::

  f(xy) = b + \sum_{i=1}^{n} w_i x_i

Each `j`th term is composed of a feature :math:`x_j` and its coeficient (aka weight) :math:`w_j` that
effectively determines the respective feature's significance.

A **bias** `b` is there to accomodate for errors in measurements.

In case if the model template has some higher order polynomials, they should
be normalized in such a way that the terms are substituted with the first order
equivalents.

Examples should be enriched with computed values for each first order equivalent.

.. note::

  If the equivalent features are computed based on multiple original features,
  it will lead to strong correlation between features or *collinearity*.

  *Collinear* features normally represent redundant information and it is a good
  idea to reformulate the model function template to avoid them.

  To verify independence rely on
  `Variance Inflation Factor <https://www.investopedia.com/terms/v/variance-inflation-factor.asp>`_.

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