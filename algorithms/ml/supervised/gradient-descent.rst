Gradient descent
================

Goal
----

Given a collection of :math:`xy` pairs, where:

- :math:`xy[i].x` is a collection of inputs (aka features),
  i.e.: :math:`xy[i].x[j]` is the individual feature
- :math:`xy[i].y` is a matching output (aka label)

, deduce a :doc:`model function <model-function>` :math:`f(x)` for which
the deviation between its prediction and the respective outputs :math:`y`
is the minimal.

Methodology
-----------

Given that a model function :math:`f(x)` can have one to many
parameters :math:`p[0], \dots, p[n]`, start at some zero point with an arbitrary set of
values assigned to each of the parameters and until the most optimal
solution is found do (aka the values converge):

**Algorithm:**
  | repeat(until_convergence) {
  |   :math:`w'_j = J_{w_j}'(xy, f)`, where :math:`j \in |w|`
  |   :math:`b' = J_{b}'(xy, f)`
  |   :math:`w_j = w_j - \alpha w'_j`, where :math:`j \in |w|`
  |   :math:`b = b - \alpha b'`
  | }

.. note::

  The most optimal solution can be a local optimum. It is not
  guaranteed that the solution will a global optimum.

  Repeat the process few times with a
  `different zero <https://machinelearningmastery.com/why-initialize-a-neural-network-with-random-weights/>`_
  to traverse a larger solution "space" to maximize the probability
  of finding the actual global optimum.
