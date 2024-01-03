Matrices
========

Matrices are **just** a way of expressing systems of linear equations.

Definition
----------

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

-  `c^i_j` are **coefficients**
-  `x^j` are **inputs**
-  `y^i` are **outputs**
-  Products of `c^i_j x_j` are **terms**

Extra terms
-----------

A single column matrix is also called a **column vector**.

A single row matrix is also called a **row vector**.

