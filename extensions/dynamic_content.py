import os

from docutils import nodes

from typing import List, Any
from types import ModuleType

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective, SphinxTranslator
from sympy import Derivative, Function, Add
from sympy.printing.latex import LatexPrinter

from importlib.util import spec_from_file_location, module_from_spec

class DynamicContent(nodes.General, nodes.Element):
    pass


MODULE_NAME = "lazy_import"


def _load_from_path(path: str) -> List[Any]:
    module_spec = spec_from_file_location(MODULE_NAME, path)
    if module_spec is None:
        return []
    loader = module_spec.loader
    if not loader:
        return []
    module = module_from_spec(module_spec)
    loader.exec_module(module)
    return _import(module)


def _load_from_content(content: str) -> List[Any]:
    module = ModuleType(MODULE_NAME, '')
    exec(content, module.__dict__)
    return _import(module)


def _import(module: ModuleType) -> List[Any]:
    return [
        getattr(module, it)
        for it in dir(module)
        if it.startswith("out")
    ]


def intToRoman(num: int):
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]

    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]

    ans = (thousands + hundreds +
           tens + ones)

    return ans


class LaconicPrinter(LatexPrinter):

    def _as_ordered_terms(self, expr: Add, order=None):
        return sorted(
            expr.args,
            key=lambda term: term.could_extract_minus_sign()
        )

    def _print_Lambdified(self, expr: Any):
        return self.doprint(expr.printed) # type: ignore

    def _print_Derivative(self, expr: Derivative):
        degree = len(expr.variables) # type: ignore

        if degree == 0:
            suffix = ""
        elif degree <= 3:
            suffix = r"\prime" * degree
        else:
            suffix = intToRoman(degree)

        main = expr.expr

        if isinstance(main, Function):
            return self._print_Function(expr.expr, suffix) # type: ignore
        else:
            return ""


def get_mathjax(expr: Any) -> str:
    res = LaconicPrinter().doprint(expr) # type: ignore
    return f"""
        <div class="math notranslate nohighlight">\\[
        {res}
        \\]</div>
    """


def visit_sympy_node_html(translator: SphinxTranslator, node: DynamicContent) -> None:
    for expr in node["expressions"]:
        translator.body.append(expr)


class Sympy(SphinxDirective):

    has_content: bool = True
    required_arguments: int = 0

    def run(self) -> List[DynamicContent]:
        if len(self.content) == 1:
            expressions = _load_from_path(os.path.join(
                self.env.srcdir,
                os.path.dirname(self.env.docname),
                self.content[0]
            ))
        elif self.content:
            expressions = _load_from_content("\n".join(self.content))
        else:
            raise ValueError("Either path or content must be specified")
        self.env.app.add_js_file(
            "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
        )
        return [DynamicContent(expressions = [get_mathjax(it) for it in expressions])]


def setup(app: Sphinx):
    app.add_node( # type: ignore
        node = DynamicContent,
        html = (visit_sympy_node_html, lambda *_: None), # type: ignore
    )
    app.add_directive("dynamic-content", Sympy)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }