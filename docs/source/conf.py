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

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

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

latex_engine = 'xelatex'

latex_documents = [
    (
        latex_test_doc,
        "sphinx-latex-reqspec-template.tex",
        "sphinx-latex-reqspec-template",
        None,
        "book",
    )
]

latex_elements = {
    "extraclassoptions": "openany,oneside",
    # The paper size ('letterpaper' or 'a4paper').
    "papersize": "a4paper",
    # 'pointsize': '14pt' # does not have any effect
    "fncychap": "",  # disable fncychap
    "releasename": "",
    "sphinxsetup": "hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
        verbatimwithframe=true, \
        TitleColor={rgb}{0,0,0}, \
        InnerLinkColor={rgb}{0.1,0.1,0.1}, \
        OuterLinkColor={rgb}{1,0,0}",
    # Roboto is also a good choice.
    # sudo apt install fonts-roboto
    "fontpkg": r"""
        \setmainfont{DejaVu Sans}
        \setsansfont{DejaVu Sans}
        \setmonofont{DejaVu Sans Mono}
    """,
    # Disable default Sphinx styles for the TOC.
    "tableofcontents": " ",
    "preamble": r"""
        \usepackage{datetime}
        \usepackage{hyperref}
        \usepackage{fancyhdr}
        \usepackage{makecell}
        \usepackage{eqparbox}
        \usepackage{titletoc}

        \setcounter{secnumdepth}{10}
        \setcounter{tocdepth}{6}

        \newdateformat{MonthYearFormat}{%
            \monthname[\THEMONTH], \THEYEAR}

        \pagecolor [RGB]{255, 255, 255}

        \hypersetup{
            colorlinks=true,
            linkcolor=[RGB]{35, 35, 35}, % color of internal links (change box color with linkbordercolor)
            citecolor=green,        % color of links to bibliography
            filecolor=magenta,      % color of file links
            urlcolor=cyan % This has an effect
        }

        \makeatletter
            % "Since the first page of a chapter uses (by design) the plain style, you need to redefine this style:"
            % https://tex.stackexchange.com/a/157006/61966
            \fancypagestyle{plain}{
                \fancyhf{}
                \fancyhead[R]{
                    \textnormal{\nouppercase{sphinx-latex-reqspec-template}}
                    \textcolor{red}{\textbf{Draft}}
                    % trim: left top
                    % \vspace*{0.4cm}{\includegraphics[trim=-1cm 1.15cm 0 -0cm, scale=.35]{bow.png}}
                }
                \fancyfoot[R]{
                    \thepage
                }
                \renewcommand{\headrulewidth}{0.0pt}
                \renewcommand{\footrulewidth}{1.0pt}
            }
            \pagestyle{plain}
            \fancypagestyle{normal}{
                \fancyhf{}
                \fancyhead[R]{
                    \textnormal{\nouppercase{sphinx-latex-reqspec-template}}
                    \textcolor{red}{\textbf{Draft}}
                    % \vspace*{0.4cm}{\includegraphics[trim=-1cm 1.15cm 0cm 0cm, scale=.35]{bow.png}}
                }
                \fancyfoot[R]{
                    \thepage
                }
                \renewcommand{\headrulewidth}{1.0pt}
                \renewcommand{\footrulewidth}{1.0pt}
            }
        \makeatother

        \titlecontents{chapter}
                      [0em]
                      {\vspace{.25\baselineskip}}
                      {\raisebox{0.038cm}{\eqparbox{ch}{\thecontentslabel}\hspace{0.2cm}}}
                      {}
                      {\titlerule*[10pt]{$\cdot$}\contentspage}

        \titlecontents{section}
                      [0.5cm]
                      {\vspace{.25\baselineskip}}
                      {\raisebox{0.038cm}{\eqparbox{S}{\thecontentslabel}\hspace{0.2cm}}}
                      {}
                      {\titlerule*[10pt]{$\cdot$}\contentspage}

        \titlecontents{subsection}
                      [1cm]
                      {\vspace{.25\baselineskip}}
                      {\raisebox{0.038cm}{\eqparbox{Ss}{\thecontentslabel}\hspace{0.2cm}}}
                      {}
                      {\titlerule*[10pt]{$\cdot$}\contentspage}

        \titlecontents{subsubsection}
                      [1.5cm]
                      {\vspace{.25\baselineskip}}
                      {\raisebox{0.038cm}{\eqparbox{Sss}{\thecontentslabel}\hspace{0.2cm}}}
                      {}
                      {\titlerule*[10pt]{$\cdot$}\contentspage}

        \titlecontents{paragraph}
                      [2cm]
                      {\vspace{.25\baselineskip}}
                      {\raisebox{0.038cm}{\eqparbox{par}{\thecontentslabel}\hspace{0.2cm}}}
                      {}
                      {\titlerule*[10pt]{$\cdot$}\contentspage}

        \titlecontents{subparagraph}
                      [2.5cm]
                      {\vspace{.25\baselineskip}}
                      {\raisebox{0.038cm}{\eqparbox{subpar}{\thecontentslabel}\hspace{0.2cm}}}
                      {}
                      {\titlerule*[10pt]{$\cdot$}\contentspage}

        \newcommand{\tablecell}[1] {{{#1}}}

        \titleformat{\chapter}[hang]
            {\normalfont\huge\bfseries}{\thechapter.}{3mm}{}
        \titlespacing*{\chapter}{0pt}{-24pt}{18pt}

        \makeatletter
            \newcommand\templatefronttitlefont{\Huge}
            \newcommand\templatefrontsubtitlefont{\@setfontsize\Huge{16}{16}}
        \makeatother
    """,
    "maketitle": RubyTemplate(
        r"""
        \begin{titlepage}
            \vspace*{50mm} %%% * is used to give space from top

            \begin{center}
                \templatefronttitlefont{\textbf{sphinx-latex-reqspec-template}}

                \vspace{5mm}

                \templatefrontsubtitlefont{{Template for requirements and specifications documents}}
            \end{center}

            \vspace{30mm}

            \begin{flushright}
                \bgroup
                    % Vertical space distribution when arraystretch is increased
                    % https://tex.stackexchange.com/a/394792/61966
                    \def\arraystretch{2}%  1 is the default, change whatever you need
                    \setlength\extrarowheight{-2pt}
                    \begin{tabular}{|p{4.85cm}|p{11.7cm}|}
                    \hline
                    \textbf{{Project goal:}} &
                    \makecell[l]{
                        A template for requirements and specifications documents.
                    }
                    \\ \hline
                    \textbf{{Target documents:}} & \tablecell {Requirements document/specification, technical manual}
                    \\ \hline
                    \textbf{{Project page:}} & \tablecell {https://github.com/stanislaw/sphinx-latex-reqspec-template}
                    \\ \hline
                    \textbf{{Release date:}} & \tablecell {\MonthYearFormat\today}
                    \\ \hline
                    \textbf{{Version:}} & \tablecell #{VERSION}
                    \\ \hline
                    \end{tabular}
                \egroup
            \end{flushright}

            %% \vfill adds at the bottom
            \vfill

            \begin{center}
                \Large{© 2021 sphinx-latex-reqspec-template}
            \end{center}

        \end{titlepage}

        \pagestyle{normal}
        \setcounter{page}{2}
        \tableofcontents
        %% \listoffigures
        %% \listoftables
        \clearpage
        """
    ).substitute(VERSION=version),
}
latex_show_urls = 'footnote'

def setup(app):
   app.add_css_file("stylesheet.css")
