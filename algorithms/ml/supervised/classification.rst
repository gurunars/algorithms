Classification
==============

Interprets regular :doc:`linear regression <linear-regression>` :math:`f(x)`
model function results as boolean values to classify the inputs.

Model function (transformed)
----------------------------

Use a sigmoid function to transform the outputs
( ``f`` is the original model function):

.. math::

    g(x) = \frac{1}{1 + e^{-f(x)}}

The nature of the function is such that:

.. math::

    0 \lt g(x) \lt 1

Effecively if:

.. math::

    g(x) = 0.5

it means, that the out output is `true` with 50% certainty.

To decide if the output is actuall `true` or `false` we need
a `boundary`:

.. code:: python

    boundary = 0.5

    def g(x: Whatever) -> float:
        ...

    verdict: bool = g(...) >= boundary

Cost function
-------------

The function for linear regression is non-convex in case of
classification. To avoid too many local optimums a different
approach is supposed to be used:

.. math::

    J(xy, f) = \frac{1}{|xy|}\sum_{i=0}^{|xy|}
     {
        -\log{
            \begin{cases}
                f(xy[i].x) & (xy[i].y == 1)
                \\
                1 - f(xy[i].x) & (xy[i].y == 0)
            \end{cases}
        }
     }

Which effectively can be rewritten as:

.. math::

    J(xy, f) = -\frac{1}{|xy|}\sum_{i=0}^{|xy|}
     {
        \log{
        \Biggl(
            \begin{split}
            (xy[i].y) * (f(xy[i].x))
            \\
            +
            \\
            (1 - xy[i].y) * (1 - f(xy[i].x))
            \end{split}
        \Biggr)
        }
     }

A partial derrivative with respect to :math:`w_j` is:

.. math::

  J_{w_j}'(xy, f) =  \frac{1}{|xy|}\sum_{i=0}^{|xy|}(f(xy[i].x) - xy[i].y) * xy[i].x[j]

A partial derrivative with respect to :math:`b` is:

.. math::

  J_{b}'(xy, f) = \frac{1}{|xy|}\sum_{i=0}^{|xy|}f(xy[i].x) - xy[i].y

.. note::

    Partial derivatives for square error and logistics cost function are the same.
    However, `f` definitions are different.