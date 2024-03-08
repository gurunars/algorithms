import os

from dataclasses import dataclass, field

from typing import List, Any, Optional, Iterable, Callable, ParamSpec, TypeVar

from sympy.plotting.plot import plot, Plot

from sympy import (
    Symbol, Function, diff, exp,
    Piecewise, ln
)

from extensions.dynamic_content import (
    get_sympy_mathjax as jax,
    local_image_file_ref as image_ref
)


def header(content: str) -> str:
    return f'<th style="font-size: 1.2em;" align="left">{content}</th>'


def td(content: str) -> str:
    return f'<td>{content}</td>'


_P = ParamSpec("_P")
_R = TypeVar("_R")


def joint(producer: Callable[_P, Iterable[str]]) -> Callable[_P, str]:
    def wrapper(*args, **kwargs) -> str: # type: ignore
        return "\n".join(producer(*args, **kwargs))
    return wrapper # type: ignore


@joint
def ul(usecases: list[str]) -> Iterable[str]:
    yield "<ul>"
    for usecase in usecases:
        yield f"<li>{usecase}</li>"
    yield "</ul>"


z = Symbol("z")

alpha = Symbol(r"\alpha")

g = Function("g")(z)


@dataclass
class FunctionDef:
    name: str
    formula: Any
    derivative: Optional[Any] = None
    usecases: list[str] = field(default_factory=list)


functions: List[FunctionDef] = [
    FunctionDef(
        "Identity",
        z,
        usecases=[
            "Identify multiple instances of specific classes (e.g. road signs on a road)"
        ]
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


def save(instance: Plot, path: str):
    rel_root = os.path.dirname(path)
    os.makedirs(rel_root, exist_ok=True)
    instance.save(path)


def row(func: FunctionDef):
    p = plot(func.formula.subs(alpha, 0.01))
    ref = image_ref(__file__, func.name, "png")
    save(p, ref.path)
    return f"""
    <tr>
        {td(func.name)}
        {td(jax(func.formula))}
        {td(jax(func.derivative or diff(func.formula, z)))}
        {td(f'<img src="{ref.url}" style="max-width: 190px;" />')}
        {td(ul(func.usecases))}
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
        {header("Usecases")}
    </tr>
    {ROWS}
</table>
"""
