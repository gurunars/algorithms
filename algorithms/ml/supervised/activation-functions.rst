Activation functions
====================

.. list-table::
   :widths: 1 1 1 1
   :header-rows: 1

   * - Name
     - Function
     - Derivative
     - Plot
   * - Identity
     - :math:`f(z) = z`
     - :math:`f'(z) = 1`
     -
   * - RelU (Rectified Linear Unit)
     -
       .. math::

         f(z) = \begin{cases}
           0 & (z \lt 0)
           \\
           z & (z \ge 0)
         \end{cases}
     -
     -
   * - Logistic (Sigmoid)
     - :math:`f(z) = \frac{1}{1 + e^{-z}}`
     - :math:`f'(z) = f(x)(1 - f(x))`
     -
   * - TanH (Hyperbolic Tangent)
     - :math:`f(z) = \frac{e^{z} - e^{-z}}{e^{z} + e^{-z}}`
     - :math:`f'(z) = 1 - f(z)^2`
     -
   * - ArcTan
     -
     -
     -
   * - Binary step
     -
     -
     -
   * - Parametric RelU
     -
     -
     -
   * - ELU (Exponential Linear Unit)
     -
     -
     -
   * - SoftPlus
     -
     -
     -
   * - Sign (Signum)
     -
     -
     -