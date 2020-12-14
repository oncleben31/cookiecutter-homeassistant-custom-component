"""Sphinx configuration."""
from datetime import datetime


project = "Home Assistant Custom Component Cookiecutter"
author = "Oncleben31"
copyright = f"{datetime.now().year}, {author}"
# extensions = ["sphinx.ext.intersphinx"]
# intersphinx_mapping = {"mypy": ("https://mypy.readthedocs.io/en/stable/", None)}
language = "en"
# html_static_path = ["_static"]
html_theme = "alabaster"
html_theme_options = {
    "github_banner": "true",
    "github_button": "true",
    "github_count": "true",
    "github_user": "oncleben31",
    "github_repo": "cookiecutter-homeassistant-custom-component",
    "github_type": "star",
    # "logo": "logo.png",
    "logo_name": "true",
    "fixed_sidebar": "true",
    "sidebar_width": "250px",
}
linkcheck_ignore = ["codeofconduct.html"]
