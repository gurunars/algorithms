Matrices
========

Matrices are **just** a way of expressing systems of linear equations.

Definition
----------

Single system of equations
^^^^^^^^^^^^^^^^^^^^^^^^^^

The following system of ``ì`` number of linear equations with
``j`` number of terms:

.. math::

    \begin{cases}
    c^1_1 * x_1 + c^1_2 * x_2 + \dots + c^1_j * x_j = y^1

    c^2_1 * x_1 + c^2_2 * x_2 + \dots + c^2_j * x_j = y^2

    \dots

    c^i_1 * x_1 + c^i_2 * x_2 + \dots + c^i_j * x_j = y^i
    \end{cases}

Is totally equvalent to the following multiplication of matrices:

.. math::

    \begin{bmatrix}
    c^1_1 & c^1_2 & \dots & c^1_j
    \\
    c^2_1 & c^2_2 & \dots & c^2_j
    \\
    \dots
    \\
    c^i_1 & c^i_2 & \dots & c^i_j
    \end{bmatrix}
    \begin{bmatrix}
    x_1
    \\
    x_2
    \\
    \dots
    \\
    x_j
    \end{bmatrix}
    =
    \begin{bmatrix}
    y^1
    \\
    y^2
    \\
    \dots
    \\
    y^i
    \end{bmatrix}

Where:

-  :math:`c^i_j` are **coefficients**
-  :math:`x^j` are **inputs**
-  :math:`y^i` are **outputs**
-  Products :math:`c^i_j * x_j` are **terms**

Multiple systems of equations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If there are multple systems of equations with identical
set of :math:`c^i_j` **coefficients** that look as follows:

.. math::

    \begin{cases}
    c^1_1 * x_{1/1} + \dots + c^1_j * x_{1/j} = y^1_1

    \dots

    c^1_1 * x_{1/1} + \dots + c^1_j * x_{1/j} = y^i_1
    \end{cases}

    \dots

    \begin{cases}
    c^1_1 * x_{e/1} + \dots + c^1_j * x_{e/j} = y^1_e

    \dots

    c^i_1 * x_{e/1} + \dots + c^i_j * x_{e/j} = y^i_e
    \end{cases}

It is identical to the following multiplication of matrices:

.. math::

    \begin{bmatrix}
    c^1_1 & \dots & c^1_j
    \\
    \dots
    \\
    c^i_1 & \dots & c^i_j
    \end{bmatrix}
    \begin{bmatrix}
    x_{1/1} & \dots & x_{e/1}
    \\
    \dots
    \\
    x_{1/j} & \dots & x_{e/j}
    \end{bmatrix}
    =
    \begin{bmatrix}
    y^1_1 & \dots & y^1_e
    \\
    \dots
    \\
    y^i_1 & \dots & y^i_e
    \end{bmatrix}

Where:

-  :math:`x_{e/j}` are **inputs** of a particular ``e`` equation
-  :math:`y_e` are **outputs** of a particular ``e`` equation

The following animation illustrates the equivalency:

.. video:: assets/equations-to-matrices.mp4
    :width: 640

Extra terms
-----------

A single column matrix is also called a **column vector**.

A single row matrix is also called a **row vector**.
