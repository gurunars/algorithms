project = 'Algorithms'
copyright = '2023, Anton Berezin'
author = 'Anton Berezin'
release = '1.0.0'
html_theme = 'sphinx_rtd_theme'
extensions = [
    'sphinxcontrib.plantuml',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.mathjax'
]
plantuml = 'java -jar ../.utils/plantuml.jar'
html_show_sphinx = False