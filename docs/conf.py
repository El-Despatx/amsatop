import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

project = 'amsatop'
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

# -- HTML output ----------------------------------------------------------
html_theme = 'alabaster'  # You can change to 'furo', 'sphinx_rtd_theme', etc.
html_static_path = ['_static']
