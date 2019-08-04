import os

from setuptools import setup, find_packages


# Package meta-data.
NAME = "{{ cookiecutter.project_name.replace(" ", "_") }}"
DESCRIPTION = "{{ cookiecutter.project_short_description }}"

# These can be set to None if you want to omit them
URL = {{ '"{}"'.format(cookiecutter.project_url) or None }}
AUTHOR = {{ '"{}"'.format(cookiecutter.full_name) or None }}
AUTHOR_EMAIL = {{ '"{}"'.format(cookiecutter.email) or None }}
LICENSE = "{{ cookiecutter.open_source_license }}"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = None  # get this from __version__.py


# What packages are required for this module to be executed?
REQUIRED = ["dash>=0.40.0", "dash-bootstrap-components>=0.3.0", "click"]

# What packages are optional?
EXTRAS = {"prod": ["mod_wsgi"]}

# get the absolute path to this file
here = os.path.abspath(os.path.dirname(__file__))


# Import the README and use it as the long-description.
# Note: this will only work if "README.md" is present in your MANIFEST.in file!
try:
    with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


# If VERSION not specified above, load the package"s __version__.py module as a
# dictionary.
about = {}
if not VERSION:
    with open(
        os.path.join(here, "src", "{{ cookiecutter.project_slug }}", "__version__.py")
    ) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=about["__version__"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={
        "": [
            "assets/favicon.ico",
            "assets/*.css",
            "assets/*.js",
            "assets/font-awesome/css/*.css",
            "assets/font-awesome/webfonts/*.eot",
            "assets/font-awesome/webfonts/*.svg",
            "assets/font-awesome/webfonts/*.ttf",
            "assets/font-awesome/webfonts/*.woff",
            "assets/font-awesome/webfonts/*.woff2",
        ]
    },
    scripts=["bin/run-{{ cookiecutter.project_slug }}-prod"],
    entry_points={
        "console_scripts": [
            "run-{{ cookiecutter.project_slug }}-dev={{ cookiecutter.project_slug }}.dev_cli:main"
        ]
    },
)
