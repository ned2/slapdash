# Slapdash

**Boilerplate for bootstrapping scalable multi-page Dash applications**

[Dash](https://plot.ly/dash) is a Python framework for building analytical web
applications. Slapdash provides a sensible project layout for quickly building
out a multi-page Dash application with room for growth. It also includes: 

* Pre-built layouts based on Bootstrap (with the help of [Dash Bootstrap
Components](https://dash-bootstrap-components.opensource.asidatascience.com)),
which can be extended or swapped out for layouts constructed using your own
Dash/CSS components.
* Scripts for conveniently launching your app in both dev and prod environments
* A URL router that helps you manage your application's pages 

This project is intended for bootstrapping initial Dash applications, rather
than being a dependency for your application. You shouldn't assume that
Slapdash's internal structure and interfaces will be stable, as they will
change.


## Boilerplate Overview

* `__init__.py` Contains helper functions for creating the Flask and Dash instances.
* `app.py` Entry point into the app. Creates both the Flask and Dash instances
  used for the app and then imports the rest of the app through the `index`
  module.
* `index.py` URL routes and the router are defined here, along with the navbar
  and its corresponding entries.
* `wsgi.py` Contains the Flask `application` attribute suitable for pointing WSGI
  servers at.
* `settings.py` Configurable settings for the application. 
* `prod_settings.py` Configurable settings for running the application in a
  production environment. Settings defined here will take precedence over those
  found in `settings.py`.
* `exceptions.py` Exceptions used by your app can be defined here.
* `components.py` Convenient Python pseudo-components are defined here.
* `utils.py` Utility things.
* `pages` The suggested project layout is to place each page of your app within
  this directory, treating each page as a modular sub-app containing a `layouts`
  attribute that you can register with the router in `index.py`.
* `assets` Location for static assets that will be exposed to the web server. 


## Installation

_Note: Slapdash requires Python 3.6+_

Slapdash is a Cookiecutter project. This means you first need to generate your
own project from the Slapdash project template. 

Install the latest Cookiecutter if you haven't installed it yet:

    pip install -U cookiecutter

Generate your project by running this command and following the prompts:

    cookiecutter https://github.com/ned2/slapdash

The resulting project is a Python package, which you then need to install like so:

    $ pip install PATH_TO_PROJECT

During development you will likely want to perform an editable install so that
changes to the source code take immediate effect on the installed package.

    $ pip install -e PATH_TO_PROJECT
    

## Usage

1. In `app.py`, select the main layout you want from `layouts.py`.
1. Create the pages of your app in different files within the `pages` directory,
   by defining within each a top-level `layout` attribute and callbacks registered
   with the Dash `app` instance from the `app`module.
1. Add the pages of your app to the URL router in`index.py`.
1. Add any desired pages to nav bar in `index.py`.
1. Modify `assets/slapdash.css` or add additional stylesheets in `assets`. 
1. Modify config in `settings.py` as required.


## The URL Router

Slapdash uses [Dash's built-in support for creating multi-page
apps](https://dash.plot.ly/urls). This involves creating a callback that targets
a container `html.Div` in your layout, and injects layout fragments into the
children property of the container when users click on links constructed with
`dcc.Link`. Slapdash provides a convenience class `DashRouter`, which assists
with the construction of this callback. The following snippet provides an
example of its use:

```python
urls = (
    ("", page1.layout),
    ("page1", page1.layout),
    ("page2", page2.layout),
    ("page3", page3.get_layout),
)

router = DashRouter(app, urls)
```

The `DashRouter` class takes as input a Dash instance, and a sequence of URL
tuples, where each tuple contains a string representing the URL endpoint for the
page as the first item, and the layout fragment to associate with that URL as
the second. The layout fragment can either be an instance of Dash's `Component`
class (such as an `html.Div`) or a callable that returns a `Component` instance,
such as the function `get_layout` in the above snippet. This callable should
take a variable number of keyword arguments, as any query parameters present in
the URL will be passed into the layout callable as keyword arguments. for
example you could pass values into the layout function below using the URL
`http://hostname?param1=value1&param2=value2`.


```python
def get_layout(**query_params):
    param1_value = query_params.get("param1", "param1 not provided")
    param2_value = query_params.get("param2", "param1 not provided")
    return html.Div([param1_value, param2_value])
```

Note that the URL endpoints will be automatically prefixed with Dash's
'routes_pathname_prefix' parameter, so when specifying internal URL links within
your layout, you will want to use `util.get_url` which prefixes the URL path for
you.


## Loading Spinners

Slapdash comes with some CSS loading spinners built-in. In order to use them,
simply add one of the classes `loader` or `loader-fade` to the component you
want to be visually rendered as loading while it is waiting for a callback to
complete. Both spinners will wait one second before being applied to avoid an
unpleasant flickering effect for responsive callbacks. The `loader` spinner will
hide the contents of the component and display a spinner, while the
`loader-fade` will reduce the opacity of the component's contents and also
display a spinner.


## Running Your App

This project comes with two convenience scripts for running your project in
development and production environments, or you can use your own WSGI server to
run the app.


### Run Dev App 

Installing this package into your virtualenv will result into the development
executable being installed into your path when the virtualenv is activated. This
command invokes your Dash app's `run_server` method, which in turn uses the
Flask development server to run your app. The command is invoked as follows,
with `proj_slug` being replaced by the value provided for this cookiecutter
parameter.

    $ run-project_slug-dev

The script takes a couple of arguments optional parameters, which you can
discover with the `--help` flag. You may need to set the port using the `--port`
parameter. If you need to expose your app outside your local machine, you will
want to set `--host 0.0.0.0`.


### Run Prod App

While convenient, the development webserver should *not* be used in
production. Installing this package will also result in a production executable
being installed in your virtualenv. This is a wrapper around the
`mod_wsgi-express` command, which streamlines use of the [mod_wsgi Apache
module](https://pypi.org/project/mod_wsgi/) to run your your app. In addition to
installing the `mod_wsgi` Python package, you will need to have installed
Apache. See installation instructions in the [mod_wsgi
documentation](https://pypi.org/project/mod_wsgi/). This script also takes a
range of command line arguments, which can be discovered with the `--help` flag.

    $ run-project_slug-prod
    
This script will also apply settings found in the module 
`project_slug.prod_settings` (or a custom Python file supplied with the 
`--settings` flag) and which takes precedence over the same settings found in 
`project_slug.settings`.

A notable advantage of using `mod_wsgi` over other WSGI servers is that we do
not need to configure and run a web server separate to the WSGI server. When
using other WSGI servers (such as Gunicorn or uWSGI), you do not want to expose
them directly to web requests from the outside world for two reasons: 1)
incoming requests will not be buffered, exposing you to potential denial of
service attacks, and 2) you will be serving your static assets via Dash's Flask
instance, which is slow. The production script uses `mod_wsgi-express` to spin
up an Apache process (separate to any process already running and listening on
port 80) that will buffer requests, passing them off to the worker processes
running your app, and will also set up the Apache instance to serve your static
assets much faster than would be the case through the Python worker processes.

_Note:_ You will need to reinstall this package in order for changes to the
prod script to take effect even if you used an editable install
(ie `pip install -e`).


### Running with a different WSGI Server

You can easily run your app using a WSGI server of your choice (such as Gunicorn
for example) with the `project_slug.wsgi` entry point
(defined in `wsgi.py`) like so:

    $ gunicorn project_slug.wsgi

_Note:_ if you want to enable Dash's debug mode while running with a WSGI server,
you'll need to export the `DASH_DEBUG` environment variable to `true`. See the
[Dev Tools](https://dash.plot.ly/devtools) section of the Dash Docs for more
details.


## Included Libraries

Slapdash includes a few libraries for getting fully functional applications off
the ground faster. These include:

* [Dash Bootstrap
  Components](https://dash-bootstrap-components.opensource.asidatascience.com/):
  A suite of Dash components that wrap Bootstrap classes, allowing for cleaner
  integration of Bootstrap with Dash layouts.
* [Bootstrap](https://getbootstrap.com) - Local copy of Bootstrap CSS files so you
  can run the app offline.
* [Font Awesome](http://fontawesome.io) - Local copy of Font Awesome files for
  offline access. Because everyone wants pretty icons.


## Useful References

1. [The Dash User Guide](https://plot.ly/dash)
   
2. [Plotly Python client figure reference](https://plot.ly/python/reference)
   Documents the contents of `plotly.graph_objs`, which contains the different
   types of charts available, as well the `Layout` class, for customising the
   appearance of charts.

3. [The Dash Community Forum](https://community.plot.ly/c/dash)

4. [Dash Show and Tell Community Thread](https://community.plot.ly/t/show-and-tell-community-thread-tada)

4. [The Dash GitHub Repository](https://github.com/plotly/dash)


## Contributing

PRs are welcome! If you have broader changes in mind, then creating an issue
first for discussion would be best.

### Seeting up a Dev Environment

After changing directory to the top level Slapdash directory:

1. Install Slapdash into your virtualenv:
    ```
    $ pip install -e .
    ```
2. Install the development requirements:
    ```
    $ pip install -r requirements-dev.txt
    ```
3. Install the pre-commit hook (for the Black code formatter)
    ```
    $ pre-commit install
    ```
