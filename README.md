# Slapdash

**Boilerplate for bootstrapping multi-page Dash applications**

[Dash](https://plot.ly/dash) is a Python framework for building analytical web
applications. Slapdash provides a template for quickly building out a multi-page
Dash application. It includes pre-built layouts based on Bootstrap, which can be
extended or swapped out for layouts constructed using your own CSS.

Also included is `dash_skeleton.py`, a template for bootstrapping smaller
single-file applications.


## Usage

This project is intended for bootstrapping initial Dash applications, as opposed
to being a package that is imported. It's internal structure and interfaces will
likely change.


## Configuration

Configurable parameters are found `settings.py`, which includes inline
descriptions.


## Included Libraries

Slapdash includes a few other dependencies for getting fully functional
applications off the ground faster. These include:

* [Bootstrap v4](https://getbootstrap.com) Just the CSS, primarily for its grid layout.
* [Font Awesome](http://fontawesome.io) Because everyone wants pretty icons.


## dash_skeleton.py

For simple applications that with a single view, the full Slapdash codebase is
probably overkill. `dash_skeleton.py` is a Dash single-file Dash template that
you can pull down and start hacking on with minimal overhead.


## Useful References

1. The Dash User Guide
   https://plot.ly/dash

2. Plotly Python client figure reference -- documents the contents of
   plotly.graph_objs, which contains the different types of charts available, as
   well the Layout class, for customising the appearance of charts.
   https://plot.ly/python/reference

3. The Dash Community Forum
   https://community.plot.ly/c/dash

4. The Dash GitHub Repository
   https://github.com/plotly/dash
