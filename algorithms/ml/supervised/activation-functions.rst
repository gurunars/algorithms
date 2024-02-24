Activation functions
====================

.. list-table::
   :widths: 1 1 1 1
   :header-rows: 1

   * - Name
     - :math:`g(z)`
     - :math:`g'(z)`
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
     - :math:`g(z)(1 - g(z))`
     -
   * - TanH (Hyperbolic Tangent)
     - :math:`\frac{e^{z} - e^{-z}}{e^{z} + e^{-z}}`
     - :math:`1 - g(z)^2`
     -
   * - Leaky RelU
     - .. math::
         \begin{cases}
           0.01z & (z \lt 0)
           \\
           z & (z \ge 0)
         \end{cases}
     - .. math::
         \begin{cases}
           0.01 & (z \lt 0)
           \\
           1 & (z \ge 0)
         \end{cases}
     -
   * - Binary step
     - .. math::
         \begin{cases}
           0 & (z \lt 0)
           \\
           1 & (z \ge 0)
         \end{cases}
     - :math:`0`
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
           g(z) + \alpha & (z \lt 0)
           \\
           1 & (z \ge 0)
         \end{cases}
     -
   * - SoftPlus
     - :math:`ln(1 + e^z)`
     - :math:`\frac{1}{1 + e^z}`
     -
