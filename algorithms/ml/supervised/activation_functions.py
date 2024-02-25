from dataclasses import dataclass

from typing import List, Any, Optional

from matplotlib.pyplot import savefig

from sympy.plotting.plot import plot

from sympy import (
    Symbol, Function, diff, exp,
    Piecewise, ln
)

from extensions.dynamic_content import get_sympy_mathjax as jax


def header(content: str) -> str:
    return f'<th style="font-size: 1.2em;" align="left">{content}</th>'


def td(content: str) -> str:
    return f'<td style="font-size: 1.1em;" >{content}</td>'


z = Symbol("z")

alpha = Symbol(r"\alpha")

g = Function("g")(z)


@dataclass
class FunctionDef:
    name: str
    formula: Any
    derivative: Optional[Any] = None


functions: List[FunctionDef] = [
    FunctionDef(
        "Identity",
        z
    ),
    FunctionDef(
        "RelU (Rectified Linear Unit)",
        Piecewise(
            (0, z < 0),
            (z, z >= 0)
        )
    ),
    FunctionDef(
        "Logistic (Sigmoid)",
        1 / (1 + exp(-z)),
        derivative=g*(1 - g)
    ),
    FunctionDef(
        "TanH (Hyperbolic Tangent)",
        (exp(z) - exp(-z)) / (exp(z) + exp(-z)),
        derivative=1 - g**2
    ),
    FunctionDef(
        "Leaky (Parametric) RelU",
        Piecewise(
            (alpha * z, z < 0),
            (z, z >= 0)
        ),
    ),
    FunctionDef(
        "Binary step",
        Piecewise(
            (0, z < 0),
            (1, z >= 0)
        )
    ),
    FunctionDef(
        "ELU (Exponential Linear Unit)",
        Piecewise(
            (alpha * (exp(z) - 1), z < 0),
            (z, z >= 0)
        )
    ),
    FunctionDef(
        "SoftPlus",
        ln(1 + exp(z))
    )
]

def row(func: FunctionDef):
    p = plot(z, func.formula.subs(alpha, 0.01))
    p.save("test.png")
    return f"""
    <tr>
        {td(func.name)}
        {td(jax(func.formula))}
        {td(jax(func.derivative or diff(func.formula, z)))}
        <td></td>
    </tr>
    """

ROWS = "\n".join(row(it) for it in functions)

out = f"""
<table class="docutils align-default">
    <tr>
        {header("Name")}
        {header(jax(g))}
        {header(jax(diff(g)))}
        {header("Plot")}
    </tr>
    {ROWS}
</table>
"""
