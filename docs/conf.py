# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sap10calcs'
copyright = '2025, Steven Firth'
author = 'Steven Firth'
release = '0.0.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'myst_parser',
]

myst_heading_anchors = 2

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_old',
                    'index.md', 'rdsap_schema_21_0_0.md', 'sap_schema_19_1_0.md']

html_extra_path = [
    'CNAME'   # This is needed to that the GitHub action copies this file to the gh-pages branch. This is used to link with the custom domain name (DNS).
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
