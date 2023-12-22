Gradient descent
================

Goal
----

Given a set of `xy` pairs, where:
 
- `xy[i].x` is an input variable (aka feature)
- `xy[i].y` is a matching output variable (aka label)
  
, deduce a model function `f(x)` whose predictions for each `xy[i].x`
has a minimal possible diviation (aka error) from `xy[i].y`.

Methodology
-----------

Given that a model function `f(x)` can have one to many implementation
attributes `A, ...`, start at some zero point with an arbitrary set of 
values assigned to each of the attributes and until the most optimal 
solution is found do:

- for each of the attributes produce a change of the smallest possible
  quantity
- from the produced attribute changes pick an `attribute to value delta`
  pair for which `f(x)` would produce the most optimal output

NOTE: the most optimal solution can be a local optimum not a global one.

Square error cost function
--------------------------

Calculates how much `f(x)` estimation diviates from the actual value `y`.

.. math::

    J(xy, f) = \frac{1}{2|xy|} \sum_{i=1}^{|xy|}(f(xy[i].x) - xy[i].y)^2
