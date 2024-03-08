Random forest
=============

Binary classification
---------------------

Entropy:

.. math::

    H(p_1) =
        \begin{cases}
            0 & (p_1 == 0 || p_1 == 1)
            \\
            -p_1 \text{log}(p_1) - (1- p_1) \text{log}(1- p_1)
        \end{cases}

Information gain:

.. math::

    \text{Information Gain} = H(p_1^\text{node})- (w^{\text{left}}H(p_1^\text{left}) + w^{\text{right}}H(p_1^\text{right}))