
project = "Camera Projection Painter"
author = "Vladlen Kuzmin (ssh4), Ivan Perevala (ivpe)"
version = "4.0.0"
copyright = "2023 BlenderHQ"

extensions = [
    "sphinx.ext.coverage",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx_design",
]

source_suffix = '.rst'
master_doc = 'index'

language = "en"
locale_dirs = ['locale/']
gettext_compact = True
gettext_location = False

html_theme = "furo"
html_static_path = ["_static"]
html_templates_path = ["_templates"]
html_favicon = "_static/favicon.ico"
html_theme_options = {
    "top_of_page_button": None,
    "light_logo": "logo-light.svg",
    "dark_logo": "logo-dark.svg",

    "light_css_variables": {
        "color-brand-primary": "black",
    },

    "dark_css_variables": {
        "color-brand-primary": "white",
    },
}
