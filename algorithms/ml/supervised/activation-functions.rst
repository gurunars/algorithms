Activation functions
====================

.. list-table::
   :widths: 1 1 1 1
   :header-rows: 1

   * - Name
     - :math:`f(z)`
     - :math:`f'(z)`
     - Plot
   * - Identity
     - :math:`z`
     - :math:`1`
     -
   * - RelU (Rectified Linear Unit)
     - .. math::
         \begin{cases}
           0 & (z \lt 0)
           \\
           z & (z \ge 0)
         \end{cases}
     - .. math::
         \begin{cases}
           0 & (z \lt 0)
           \\
           1 & (z \ge 0)
         \end{cases}
     -
   * - Logistic (Sigmoid)
     - :math:`\frac{1}{1 + e^{-z}}`
     - :math:`f(z)(1 - f(z))`
     -
   * - TanH (Hyperbolic Tangent)
     - :math:`\frac{e^{z} - e^{-z}}{e^{z} + e^{-z}}`
     - :math:`1 - f(z)^2`
     -
   * - Binary step
     -
     -
     -
   * - Parametric RelU
     - .. math::
         \begin{align*}
           \begin{cases}
             \alpha z & (z \lt 0)
             \\
             z & (z \ge 0)
           \end{cases}
         \end{align*}
     - .. math::
         \begin{cases}
           \alpha & (z \lt 0)
           \\
           1 & (z \ge 0)
         \end{cases}
     -
   * - ELU (Exponential Linear Unit)
     - .. math::
         \begin{cases}
           \alpha (e^z - 1) & (z \lt 0)
           \\
           z & (z \ge 0)
         \end{cases}
     - .. math::
         \begin{cases}
           f(z) + \alpha & (z \lt 0)
           \\
           1 & (z \ge 0)
         \end{cases}
     -
   * - SoftPlus
     - :math:`ln(1 + e^z)`
     - :math:`\frac{1}{1 + e^z}`
     -
   * - Sign (Signum)
     -
     -
     -