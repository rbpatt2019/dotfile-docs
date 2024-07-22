"""Sphinx configuration."""

import os
import sys

sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.abspath("./"))

project = "rbpatt2019's dotfiles'"
author = "rbpatt2019 <rb.patterson.cross@gmail.com>"
project_copyright = "Ryan B Patterson-Cross 2024"
version = "1"  # Refers to the build of the docs only
extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx_tabs.tabs",
]
pygments_style = "sphinx"

html_logo = "_static/dragon-solid.svg"
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/rbpatt2019/dotfile-docs",
    "repository_branch": "main",
    "path_to_docs": "docs",
    "use_repository_button": True,
    "use_source_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "icon_links": [
        {
            "name": "Github",
            "url": "https://github.com/rbpatt2019/dotfile-docs",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
        {
            "name": "NixOS",
            "url": "https://nixos.org/",
            "icon": "https://img.shields.io/badge/Nix-5277C3.svg?&logo=NixOS&logoColor=white",
            "type": "url",
        },
        {
            "name": "Stars",
            "url": "https://github.com/rbpatt2019/dotfile-docs/stargazers",
            "icon": "https://img.shields.io/github/stars/rbpatt2019/dotfile-docs",
            "type": "url",
        },
    ],
}

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
