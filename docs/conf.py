"""Sphinx configuration."""

import os
import sys

sys.path.insert(0, os.path.abspath("../"))

project = "rbpatt2019's dotfiles'"
author = "Ryan B Patterson-Cross <rb.patterson.cross@gmail.com>"
project_copyright = "Ryan B Patterson-Cross 2024"
version = "1"  # Refers to the build of the docs only
extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx_tabs.tabs",
]
pygments_style = "sphinx"
html_theme = "sphinx_book_theme"

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
