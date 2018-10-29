# Slapdash

**Boilerplate for bootstrapping multi-page Dash applications**

_Note: This is a work in progress, but it's probably at a point where it's
more useful than not._

[Dash](https://plot.ly/dash) is a Python framework for building analytical web
applications. Slapdash provides a template for quickly building out a multi-page
Dash application. It includes pre-built layouts based on Bootstrap, which can be
extended or swapped out for layouts constructed using your own CSS.

Note that this project is intended for bootstrapping initial Dash applications,
as opposed to being a library that you depend upon by importing. You probably
shouldn't assume that its internal structure and interfaces will be stable, as
they will likely change.

Also included is `dash_skeleton.py`, a minimal template for bootstrapping
smaller single-file applications.


## Installation

After cloning/downloading the repository, simply install Slapdash as a package like this into your target virtualenv:

    cd <PATH_TO_SLAPDASH>
    pip install -e .

## Usage

1. In `app.py`, select the main layout you want from `layouts.py`.
2. Create your callbacks in `callbacks.py`.
3. Create  your pages in `pages.py`.
4. Add your pages to the `urls` attribute in `router.py`.
5. Add desired pages to `NAV_ITEMS` (if using a navbar) in `settings.py`.
6. Add additional CSS to `assets/custom.css`. 
7. Modify any additional settings in settings.py as desired. (The only other one
   you will likely definitely need to change is TITLE).


## Running Your App

You can launch the app using the `run_flask.py` script, which uses Flask's development server (and which shouldn't be used in production). The script takes a couple of arguments optional parameters, which you can discover with `--help` flag.

    $ python run_flask.py --debug

You can run your app using a WSGI server (such as Gunicorn) with the `wsgi.py` entry point like so:

    $ gunicorn slapdash.wsgi

Or if you'd rather not install the Slapdash package, relative to the root directory: 

    $ gunicorn src.slapdash.wsgi
    
    
## Boilerplate Overview

* `app.py` Entry point into the app. Imports other modules in correct order. 
* `server.py` Creates both the Flask server and Dash app instances used for the app.
* `callbacks.py` Custom callbacks go here.
* `layouts.py` Possible values for the `layout` attribute of the Dash instance
  are defined here.
* `pages.py` Custom pages go here.
* `wsgi.py` Contains `application` attribute suitable for pointing WSGI servers at.
* `settings.py` Configurable settings for the application. 
* `router.py` Contains the application routes in url and initialises the router callback.
* `exceptions.py` Exceptions used by the app are defined here.
* `components.py` Convenient Python pseudo-components defined here, such as `Row` and
  `Col` for an easy experience creating Bootstrap rows and columns.
* `utils.py` Utility things defined here.
* `assets` Location for static assets that will be exposed to the web server. 


## Included Libraries

Slapdash includes a few plugins for getting fully functional applications off
the ground faster. These currently include:

* [Bootstrap v4](https://getbootstrap.com) Just the CSS, primarily for its grid layout.
* [Font Awesome](http://fontawesome.io) Because everyone wants pretty icons.


## dash_skeleton.py

For simple applications that with a single view, the full Slapdash codebase is
probably overkill. `dash_skeleton.py` is a Dash single-file Dash template that
you can pull down and start hacking on with minimal overhead.


## Useful References

1. [The Dash User Guide](https://plot.ly/dash)
   
2. [Plotly Python client figure reference](https://plot.ly/python/reference)
   Documents the contents of plotly.graph_objs, which contains the different
   types of charts available, as well the Layout class, for customising the
   appearance of charts.

3. [The Dash Community Forum](https://community.plot.ly/c/dash)

4. [Dash Show and Tell Community Thread](https://community.plot.ly/t/show-and-tell-community-thread-tada)

4. [The Dash GitHub Repository](https://github.com/plotly/dash)
