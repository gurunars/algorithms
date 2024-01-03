Cost function
=============

Given a :doc:`model function <model-function>` :math:`f(x)` and the actual outcome :math:`f(x)`,
the function that determines the error factor between the prediction and the actual outcome
is called a *cost function* :math:`J(xy, f)`.

Squared error cost function
---------------------------

A **conventionally** used cost function.

.. math::

  J(xy, f) = \frac{\sum_{i=0}^{|xy|}(f(xy[i].x) - xy[i].y)^2}{2|xy|}

A partial derrivative with respect to :math:`w_j` is:

.. math::

  J_{w_j}'(xy, f) =  \frac{\sum_{i=0}^{|xy|}(f(xy[i].x) - xy[i].y) * xy[i].x[j]}{|xy|}

A partial derrivative with respect to :math:`b` is:

.. math::

  J_{b}'(xy, f) = \frac{\sum_{i=0}^{|xy|}f(xy[i].x) - xy[i].y}{|xy|}
