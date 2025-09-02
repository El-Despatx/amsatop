import os
import sys

sys.path.insert(0, os.path.abspath('../src'))

project = 'amsatop'
copyright = '2025'
release = '0.3.0'

extensions = [
    'sphinx.ext.autodoc',          # Include documentation from docstrings
    'sphinx.ext.napoleon',         # Support for Google/NumPy docstrings
    'sphinx.ext.viewcode',         # Add links to highlighted source code
    'sphinx.ext.autosummary',      # Generate summary tables
]

autosummary_generate = True  # Turn on autosummary generation

templates_path = ['_templates']
exclude_patterns = []

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# -- HTML output ----------------------------------------------------------
# html_theme = 'alabaster'  # You can change to 'furo', 'sphinx_rtd_theme', etc.
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
