Gradient descent
================

Goal
----

Given a collection of ``xy`` pairs, where:
 
- ``xy[i].x`` is a collection of inputs (aka features),
  i.e.: ``xy[i].x[j]`` is the individual feature
- ``xy[i].y`` is a matching output (aka label)
  
, deduce a model function ``f(x)`` whose predictions for ``xy.map { it.x }``
has a minimal possible deviation (aka error) from ``xy.map { it.y }``.
The function that determines the error size is ``J(xy, f)`` and is
called an error function.

Methodology
-----------

Given that a model function ``f(x)`` can have one to many 
parameters ``p[0], .., p[n]``, start at some zero point with an arbitrary set of 
values assigned to each of the parameters and until the most optimal 
solution is found do (aka the values converge):

- for each of the parameters produce a change pair of the smallest possible
  quantity. Thei pair would look as ``parameter to new_value``.

  .. math::

    new\_p = p.map \{ it - delta \}

- from the produced collection of change pairs pick an such a
  pair for which ``f(x)`` would produce the most optimal output.

NOTE: the most optimal solution can be a local optimum. It is not
guaranteed that the solution will a global optimum.

Square error cost function
--------------------------

Calculates how much ``f(x)`` estimation deviates from the actual output
value ``y``.

.. math::

    J(xy, f) = \frac{1}{2|xy|} \sum_{i=1}^{|xy|}(f(xy[i].x) - xy[i].y)^2
