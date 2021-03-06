# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('_ext'))
import os
on_rtd = os.environ.get('READTHEDOCS') == 'True'

# -- Project information -----------------------------------------------------

project = ''
copyright = '2021, Quentin Ra'
author = 'Quentin Ra'

# The full version, including alpha/beta/rc tags
release = 'build-3.44.615'
# version 0 : fait en html, css, php, js
# version 1 : refonte mais en restructured text avec sphinx
# version 1.1 : system/docker
# version 1.2 : utils/vim
# version 1.3 : maths/graphes
# version 1.4 : conception/ihm
# version 1.5 : maths/matrix
# version 1.6 : db/sql
# version 1.7 : db/plsql
# version 1.8 : conception/classes
# version 1.9 : conception/usage
# version 1.10 : conception/sequence
# version 1.11 : conception/objets
# version 1.12 : conception/bd
# version 1.13 : conception/automate
# version 1.14 : conception/mdd ===> conception/me
# version 1.15 : conception/patrons
# version 1.16 : db/model
# version 1.17 : team/agile
# version 1.18 : team/gestion
# version 1.19 : team/cdc
# version 1.20 : imperative/c
# version 1.21 : business/insertion
# version 1.22 : business/macro
# version 1.23 : business/docs
# version 1.24 : system/arm
# version 1.25 : system/cyber
# version 1.26 : business/cesim
# version 2+ => nouvelle doc
# version 2.27 : db/cypher
# version 2.28 : business/com
# version 3+ => début du clean
# version 3.29 : maths/analyse
# version 3.30 : utils/git
# version 3.31 : utils/rst
# version 3.32 : system/linux
# version 3.33 : system/bash
# version 3.34 : imperative/java
# version 3.35 : web/html
# version 3.36 : web/css
# version 3.37 : system/net
# version 3.38 : web/mdb
# version 3.39 : web/general
# version 3.40 : web/php
# version 3.41 : conception/tests
# version 3.42 : web/js
# version 3.43 : functional/ocaml
# version 3.44 : conception/me/doxygen

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# note for pip3.8
import sphinx_rtd_theme
extensions = [
'recommonmark',
"sphinx_rtd_theme", 'sphinx.ext.graphviz',
'sphinxcontrib.plantuml'
,'matplotlib.sphinxext.plot_directive',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'fr'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md',
'.github/CONTRIBUTING.md',
'.github/ISSUE_TEMPLATE/bug_report.md',
'.github/ISSUE_TEMPLATE/feature_request.md',
'.github/PULL_REQUEST_TEMPLATE/pull_request_template.md',
'.github/SECURITY.md',
'.github/CODE_OF_CONDUCT.md',
'.github/INSTALL.md',
]

html_css_files = [
    'css/light.css',
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['assets']

html_show_sourcelink = False
html_favicon = 'assets/favicon.png'
# html_logo = 'assets/cr.png'

# https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
html_theme_options = {
  'display_version': True,
	#'style_nav_header_background' : '#FFCC00'
}

# -- edit on github ----------------------------------

html_context = {}
html_context['display_github'] = True
html_context['github_user'] = 'QuentinRa'
html_context['github_repo'] = 'ramsamy.ws-res'
html_context['github_version'] = 'master/'

# -- GraphViz configuration ----------------------------------
import shutil

if shutil.which("dot") == None :
	graphviz_dot="C:/graphviz/bin/dot.exe"

graphviz_output_format = 'svg'

# -- PDF

pdf_documents = [('index', u'memorize', u'Memorize', u'Quentin Ra')]

# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output
# https://docs.readthedocs.io/en/stable/guides/pdf-non-ascii-languages.html
latex_engine = 'xelatex'

# -- plantuml
# https://github.com/sphinx-contrib/plantuml/

if shutil.which("plantuml") == None :
	plantuml="java -jar C:/graphviz/bin/plantuml.jar"

# plots
# https://matplotlib.org/3.1.3/devel/plot_directive.html
plot_include_source=False