Linear regression
=================

Model function
--------------

The function is always a first order polynomial with `j` terms augumented by a **bias** parameter `b`:

.. math::

  f(b, w, xy) = b + \sum_{j=0}^{|w|} w_j x_j

Each `j`'th term is composed of a feature :math:`x_j` and its coeficient (aka weight) :math:`w_j` that
effectively determines the respective feature's significance.

A **bias** `b` is there to accomodate for errors in measurements.

In case if the model template has some higher order polynomials, they should
be normalized in such a way that the terms are substituted with the first order
equivalents.

Examples should be enriched with computed values for each first order equivalent.

Cost function
-------------

Given a model function :math:`f(x)` and the actual outcome :math:`f(x)`
determines the error factor between the prediction and the actual outcome.

.. math::

  J(xy, f) = \frac{1}{|xy|}\sum_{i=0}^{|xy|}\frac{1}{2}(f(xy[i].x) - xy[i].y)^2

A partial derrivative with respect to :math:`w_j` is:

.. math::

  J_{w_j}'(xy, f) =  \frac{1}{|xy|}\sum_{i=0}^{|xy|}(f(xy[i].x) - xy[i].y) * xy[i].x[j]

A partial derrivative with respect to :math:`b` is:

.. math::

  J_{b}'(xy, f) = \frac{1}{|xy|}\sum_{i=0}^{|xy|}f(xy[i].x) - xy[i].y


Regularization
--------------

Fights against overfitting by penalizing too large values of :math:`w_j`
within a cost function.

Due to the fact that it is unknown which :math:`w_j` is more important,
the regularization term needs to include all of them:

.. math::

    r(w, xy, \lambda) = \frac{\lambda}{2|xy|}\sum_{i=0}^{|w|}w^2_j

The term has to be appended to the original model function:

.. math::

    {\sim}J(b, w, xy, \lambda) = J(b, w, xy) + r(w, xy, \lambda)

A partial derrivative with respect to :math:`w_j` is:

.. math::

    {\sim}J'_j(b, w, xy, \lambda) =
        \frac{\lambda}{|xy|} +
        \frac{1}{|xy|}\sum_{i=0}^{|xy|}(f(xy[i].x) - xy[i].y) * xy[i].x[j]

:math:`b` does not need regularization.