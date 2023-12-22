Linear Regression
=================

Given a set of `xy` pairs, where:
 
- `xy[i].x` is an input variable
- `xy[i].y` is a matching output variable
  
, deduce a model function `f(x)` whose predictions for each `xy[i].x`
has a minimal possible diviation (aka error) from `xy[i].y`.

Square error cost function
--------------------------

Calculates how much `f(x)` estimation diviates from the actual value `y`.

.. math::

    J(xy, f) = \frac{1}{2|xy|} \sum_{i=1}^{|xy|}(f(xy[i].x) - xy[i].y)^2
