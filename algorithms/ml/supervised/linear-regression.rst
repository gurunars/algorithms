Linear Regression
=================

Square error cost function
--------------------------

Calculates how much the prediction diviates from the actual value from a dataset.

.. math::

    f(w, b, x) = wx + b

    e(w, b, xy) = \frac{1}{2|xy|} \sum_{i=1}^{|xy|}(f(w, b, xy[i].x) - xy[i].y)^2