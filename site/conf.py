# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Sam's Notes"
copyright = '2023, Samuel James Williams'
author = 'Samuel James Williams'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
]

myst_enable_extensions = ["dollarmath"]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#

html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
html_theme_options = {
    "logo": {
        "text": "Sam's notes",
    }
}