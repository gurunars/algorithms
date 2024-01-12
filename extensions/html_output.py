import os

from docutils import nodes

from typing import List

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective, SphinxTranslator
from subprocess import check_output


class HtmlOutputNode(nodes.General, nodes.Element):
    pass


def visit_html_node_html(translator: SphinxTranslator, node: HtmlOutputNode) -> None:
    translator.body.append(
        check_output(["python", node["path"]]).decode("utf-8")
    )


class HtmlOutput(SphinxDirective):

    has_content: bool = True
    required_arguments: int = 1

    def run(self) -> List[HtmlOutputNode]:
        self.env.app.add_js_file(
            "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
        )
        return [HtmlOutputNode(
            path=os.path.join(
                self.env.srcdir,
                os.path.dirname(self.env.docname),
                self.arguments[0]
            )
        )]


def setup(app: Sphinx):
    app.add_config_value("path", "", "html")
    app.add_node( # type: ignore
        node = HtmlOutputNode,
        html = (visit_html_node_html, lambda *_: None), # type: ignore
    )
    app.add_directive("html-output", HtmlOutput)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }