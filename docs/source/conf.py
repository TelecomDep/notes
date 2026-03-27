# Configuration file for the Sphinx documentation builder.


"""
Imports the system and the 
theme the project is using to the project.
"""

import string
import sys, os
import sphinx_bootstrap_theme

"""
Adds path to the folder ext, where extensions are stored.
"""

sys.path.append(os.path.abspath('ext'))
sys.path.append('.')

"""
Tells Sphinx which extensions to use.
"""
extensions = [
    'myst_nb',
    'myst_parser',
    'sphinxcontrib.mermaid',
    'sphinxcontrib.wavedrom',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.tikz',
    'sphinxcontrib.blockdiag',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.graphviz',
    'sphinxcontrib.exceltable',
]


class RubyTemplate(string.Template):
    delimiter = "#"
    
# -- Project information

project = 'Telecom Notes'
copyright = '2025, ...'
author = '...'

release = '0.1'
version = '0.1.0'


mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
myst_enable_extensions = ["dollarmath"]

# Optional: Configure MathJax 3 if needed
mathjax3_config = {
    "tex": {
        "inlineMath": [['\\(', '\\)']],
        "displayMath": [['\\[', '\\]']],
    }
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst']

# The master toctree document.
master_doc = 'index'
latex_test_doc = 'usage'

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_theme_options = {
    "project_nav_name": "sphinx-latex-reqspec-template",
}


def setup(app):
   app.add_css_file("stylesheet.css")

