import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ACC-DTAF-APIs'
copyright = '2023, Fang'
author = 'Fang'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        'recommonmark',
        'sphinx.ext.autodoc',
        'sphinx.ext.viewcode',
]
templates_path = ['_templates']
exclude_patterns = []
source_suffix = ['.rst', '.md', '.MD']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'furo'
html_static_path = ['_static']
