# Briefcase documentation build configuration file, created by
# sphinx-quickstart on Sat Jul 27 14:58:42 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys
from importlib.metadata import version as metadata_version

import beeware_theme

# BeeWare theme override for Furo Sphinx theme to add BeeWare features.
templates_path = []
html_static_path = []
html_css_files = []
html_context = {}
html_theme_options = {}

beeware_theme.init(
    project_name="briefcase",
    templates=templates_path,
    context=html_context,
    static=html_static_path,
    css=html_css_files,
    theme_options=html_theme_options,
)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("../src"))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx_tabs.tabs",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.spelling",
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "Briefcase"
copyright = "Russell Keith-Magee"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags
release = metadata_version("briefcase")
# The short X.Y version
version = ".".join(release.split(".")[:2])

autoclass_content = "both"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

# API status indicators.
rst_prolog = """
.. role:: full
.. role:: yes
.. role:: ymmv
.. |f| replace:: :full:`●`
.. |y| replace:: :yes:`○`
.. |v| replace:: :ymmv:`△`
"""

# -- Options for link checking -------------------------------------------------

linkcheck_anchors_ignore = [
    # Ignore anchor detection/verification for Apple help links
    # e.g.: https://help.apple.com/xcode/mac/current/#/dev97211aeac
    "^/dev[0-9a-f]{9}$"
]

linkcheck_ignore = [
    r"^./android/gradle.html$",
    r"^./iOS/xcode.html$",
    r"^./linux/appimage.html$",
    r"^./linux/flatpak.html$",
    r"^./linux/system.html$",
    r"^./macOS/app.html$",
    r"^./macOS/xcode.html$",
    r"^./web/static.html$",
    r"^./windows/app.html$",
    r"^./windows/visualstudio.html$",
    r"^https://github.com/beeware/briefcase/issues/\d+$",
    r"^https://github.com/beeware/briefcase/pull/\d+$",
    # Ignore WiX URLs, because they client block RTD's build.
    r"^https://www.firegiant.com/wixtoolset/$",
    # PyGame seems to be having a long-term outage of their homepage.
    r"^https://www.pygame.org/news$",
]

# -- Options for copy button ---------------------------------------------------

# virtual env prefix: (venv), (beeware-venv), (testenv)
venv = r"\((?:(?:beeware-)?venv|testvenv)\)"
# macOS and Linux shell prompt: $
shell = r"\$"
# win CMD prompt: C:\>, C:\...>
cmd = r"C:\\>|C:\\\.\.\.>"
# PowerShell prompt: PS C:\>, PS C:\...>
ps = r"PS C:\\>|PS C:\\\.\.\.>"
# zero or one whitespace char
sp = r"\s?"

# optional venv prefix
venv_prefix = rf"(?:{venv})?"
# one of the platforms' shell prompts
shell_prompt = rf"(?:{shell}|{cmd}|{ps})"

copybutton_prompt_text = "|".join(
    [
        # Python REPL
        # r">>>\s?", r"\.\.\.\s?",
        # IPython and Jupyter
        # r"In \[\d*\]:\s?", r" {5,8}:\s?", r" {2,5}\.\.\.:\s?",
        # Shell prompt
        rf"{venv_prefix}{sp}{shell_prompt}{sp}",
    ]
)
copybutton_prompt_is_regexp = True
copybutton_remove_prompts = True
copybutton_only_copy_prompt_lines = True
copybutton_copy_empty_lines = False

# -- Options for HTML output ---------------------------------------------------

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = f"Briefcase {release}"

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/images/briefcase.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path.append("_static")

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "briefcasedoc"

html_theme = "furo"

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (
        "index",
        "briefcase.tex",
        "Briefcase Documentation",
        "Russell Keith-Magee",
        "manual",
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ("index", "briefcase", "Briefcase Documentation", ["Russell Keith-Magee"], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "briefcase",
        "Briefcase Documentation",
        "Russell Keith-Magee",
        "Briefcase",
        "Tools to support development of Python on mobile platforms.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# -- Options for spelling -------------------------------------------
# Spelling language.
spelling_lang = "en_US"

# Location of word list.
spelling_word_list_filename = "spelling_wordlist"

# -- Options for Todos -------------------------------------------

# If this is True, todo and todolist produce output, else they produce nothing. The default is False.
todo_include_todos = True

# If this is True, todo emits a warning for each TODO entries. The default is False.
# todo_emit_warnings = False

# If this is True, todolist produce output without file path and line, The default is False.
# todo_link_only = False
