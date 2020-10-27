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

# -- Project information -----------------------------------------------------

project = 'ramsamy.ws/ressources'
copyright = '2020, Quentin Ra'
author = 'Quentin Ra'

# The full version, including alpha/beta/rc tags
release = '1.2.35'
# version 0 : html, css, php, js
# version 1 : restructured text
# version 1.1 : docker
# version 1.2 : vim

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import sphinx_rtd_theme
extensions = ['recommonmark', "sphinx_rtd_theme", 'sphinx.ext.graphviz']

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
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'Readme.md',
'.github/CONTRIBUTING.md',
'.github/ISSUE_TEMPLATE/bug_report.md',
'.github/ISSUE_TEMPLATE/feature_request.md',
'.github/PULL_REQUEST_TEMPLATE/pull_request_template.md',
'.github/SECURITY.md',
'.github/CODE_OF_CONDUCT.md',
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

# -- edit on github ----------------------------------

html_context = {}
html_context['display_github'] = True
html_context['github_user'] = 'QuentinRa'
html_context['github_repo'] = 'ramsamy.ws-res'
html_context['github_version'] = 'master/'

# -- GraphViz configuration ----------------------------------

graphviz_dot='C:/graphviz/bin/dot.exe'
graphviz_output_format = 'svg'