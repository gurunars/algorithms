from dataclasses import dataclass

from typing import List, Any

from sympy import Symbol, Function, diff

from extensions.dynamic_content import get_sympy_mathjax as jax


def header(content: str) -> str:
    return f'<th style="font-size: 1.2em;" align="left">{content}</th>'


z = Symbol("z")

@dataclass
class FunctionDef:
    name: str
    formula: Any

functions: List[FunctionDef] = [
    FunctionDef("Identity", z)
]

def row(func: FunctionDef):
    return f"""
    <tr>
        <td>{func.name}</td>
        <td>{jax(func.formula)}</td>
        <td>{jax(diff(func.formula, z))}</td>
        <td></td>
    </tr>
    """


out = f"""
<table class="docutils align-default">
    <tr>
        {header("Name")}
        {header(jax(Function("g")(z)))}
        {header(jax(Function("g'")(z)))}
        {header("Plot")}
    </tr>
    {
        "\n".join(
            row(it) for it in functions
        )
    }
</table>
"""
