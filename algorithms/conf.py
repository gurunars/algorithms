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
    'sphinx.ext.mathjax',
    "sphinxcontrib.video",
    'extensions.dynamic_content',
    'sphinxcontrib.rawfiles',
    'matplotlib.sphinxext.plot_directive'
]
plantuml = 'java -jar ../.utils/plantuml.jar'
html_show_sphinx = False
rawfiles = [
    "maths/assets"
]
html_show_sourcelink = False
suppress_warnings = ['autosectionlabel.*']
mathjax3_config = {'chtml': {'displayAlign': 'left'}}
plot_html_show_source_link = False
plot_html_show_formats = False
html_static_path = ['_static']

def setup(app):
    app.add_css_file('algorithms.css')