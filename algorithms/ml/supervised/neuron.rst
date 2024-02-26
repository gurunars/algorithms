Neuron
======

Visually it looks as follows:

.. graphviz::

  digraph neuron {
    rankdir="LR";
    node [shape=circle]


    w1 [label=<W<SUB>1</SUB>>];
    x1 [label=<X<SUB>1</SUB>>];
    w2 [label=<W<SUB>2</SUB>>];
    x2 [label=<X<SUB>2</SUB>>];
    w [label=<W<SUB>...</SUB>>];
    x [label=<X<SUB>...</SUB>>];
    wm [label=<W<SUB>m</SUB>>];
    xm [label=<X<SUB>m</SUB>>];

    sum [label=<&#8721;>];

    g [label=<g(z)>];

    subgraph clusterinputs{
      label="Inputs"
      x1;x2;x;xm;
    }

    subgraph clusterweights{
      label="Weights"
      w1;w2;w;wm;
    }

    subgraph clusterbias{
      label="Bias"
      b;
    }

    subgraph clusterg{
      label="Activation Function"
      g;
    }

    subgraph clustery{
      label="Output"
      y;
    }

    subgraph clustersum{
      label="Linear Combinder"
      sum;
    }

    subgraph params {
      edge [dir=none];

      x1 -> w1 [label="*"];
      x2 -> w2 [label="*"];
      x -> w [label="*"];
      xm -> wm [label="*"];
    }

    w1 -> sum;
    w2 -> sum;
    w -> sum;
    wm -> sum;

    sum -> b [label="+"];

    b -> g [label="|"];

    g -> y [label="="];
  }

Or as a simple function:

.. math::

  z = \sum_{j=1}^{m} w_j x_j + b

  y = g(z)