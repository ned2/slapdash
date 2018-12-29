# Slapdash

**Boilerplate for bootstrapping scalable multi-page Dash applications**

[Dash](https://plot.ly/dash) is a Python framework for building analytical web
applications. Slapdash provides a sensible project layout for quickly building
out a multi-page Dash application with room for growth. It includes pre-built
layouts based on Bootstrap (with the help of [Dash Bootstrap
Components](https://dash-bootstrap-components.opensource.asidatascience.com)),
which can be extended or swapped out for layouts constructed using your own
Dash/CSS components.

This project is intended for bootstrapping initial Dash applications, rather
than being a dependency for your application. You shouldn't assume that
Slapdash's internal structure and interfaces will be stable, as they will
change.


## Installation

After cloning/downloading the repository, simply install Slapdash as a package
into your target virtualenv:

    cd <PATH_TO_SLAPDASH>
    pip install -e .

## Usage

1. In `app.py`, select the main layout you want from `layouts.py`.
1. Create the pages of your app in different files within the `pages` directory,
   by defining within each a top-level `layout` attribute and callbacks registered
   with the Dash `app` instance from the `app`module.
1. Add your pages to the `URLS` attribute in `index.py`.
1. Add desired pages to the `NAV_ITEMS` attribute in `index.py`.
1. Modify `assets/slapdash.css` or add additional stylesheets in `assets`. 
1. Modify config in `settings.py` as required.


## Running Your App

You can launch the app using the `run-flask.py` script, which uses Flask's
development server (and which shouldn't be used in production). The script takes
a couple of arguments optional parameters, which you can discover with the
`--help` flag. The `--debug` flag is particularly useful, activating the Dash
dev tools, including hot reloading.

    $ python run-flask.py --debug

You can run your app using a WSGI server (such as Gunicorn) with the `wsgi.py`
entry point like so:

    $ gunicorn slapdash.wsgi

Or if you'd rather not install the Slapdash package, relative to the root directory: 

    $ gunicorn src.slapdash.wsgi

Note: if you want to enable Dash's debug mode while running with a WSGI server,
you'll need to set the `DASH_DEBUG` environment variable to `true`. See the [Dev
Tools](https://dash.plot.ly/devtools) section of the Dash Docs for more details.


## Boilerplate Overview

* `__init__.py` Contains helper functions for creating the Flask and Dash instances.
* `app.py` Entry point into the app. Creates both the Flask and Dash instances
  used for the app and then imports the rest of the app through the `index`
  module.
* `index.py` Contains the URL routes and corresponding callback router, as well
as the entries to be used for the nav bar, along with the corresponding callback
for the nav bar.
* `wsgi.py` Contains the Flask `application` attribute suitable for pointing WSGI
  servers at.
* `settings.py` Configurable settings for the application. 
* `exceptions.py` Exceptions used by your app can be defined here.
* `components.py` Convenient Python pseudo-components are defined here.
* `utils.py` Utility things.
* `pages` The suggested project layout is to place each page of your app within
  this directory, treating each page as a modular sub-app with a `layouts`
  attribute that you can register with the router in `index.py`.
* `assets` Location for static assets that will be exposed to the web server. 


## Included Libraries

Slapdash includes a few libraries for getting fully functional applications off
the ground faster. These include:

* [Bootstrap](https://getbootstrap.com) - Just the CSS.
* [Dash Bootstrap
  Components](https://dash-bootstrap-components.opensource.asidatascience.com/)
   - A suite of Dash components that wrap Bootstrap classes, allowing for cleaner
  integration of Bootstrap with Dash layouts.
* [Font Awesome](http://fontawesome.io) - Because everyone wants pretty icons.


## Useful References

1. [The Dash User Guide](https://plot.ly/dash)
   
2. [Plotly Python client figure reference](https://plot.ly/python/reference)
   Documents the contents of `plotly.graph_objs`, which contains the different
   types of charts available, as well the `Layout` class, for customising the
   appearance of charts.

3. [The Dash Community Forum](https://community.plot.ly/c/dash)

4. [Dash Show and Tell Community Thread](https://community.plot.ly/t/show-and-tell-community-thread-tada)

4. [The Dash GitHub Repository](https://github.com/plotly/dash)
