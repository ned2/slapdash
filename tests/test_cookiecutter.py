import subprocess
import sys
from importlib import import_module, invalidate_caches


def install_package(package):
    """Install the supplied package into the current environment."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    
def bake_install_and_get_app_module(cookies, project_name="test_app"):
    """Bake the recipe, install the package, and return the `app` module"""
    result = cookies.bake(extra_context={"project_name": project_name})
    install_package(result.project)
    invalidate_caches()
    app_module = import_module(".app", package=project_name)
    return app_module


def test_bake_project(cookies, project_name="test_app"):
    """Test that the cookiecutter recipe is baked."""
    result = cookies.bake(extra_context={"project_name": project_name})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.isdir()
    assert result.project.basename == project_name


# TODO: verify that this fails when app has an error (ie 500 response)
def test_baked_project_runs(cookies, dash_thread_server):
    """Test that the Dash app in the baked project runs."""
    app_module = bake_install_and_get_app_module(cookies)
    dash_thread_server.start(app_module.app)
    # TODO: use dash_thread_server.accessible() to check for each
    # url from index.py
    

# TODO: this needs to be parameterised to only be run when
# some kind of webdriver flag is passed to not make the basic tests rely
# on having a webdriver installed
def test_baked_project_runs_webdriver(cookies, dash_duo):
    """Test that the Dash app in the baked project runs."""
    app_module = bake_install_and_get_app_module(cookies)
    dash_duo.start_server(app_module.app)

    assert dash_duo.get_logs() == [], "browser console should contain no error"
    # TODO:
    # - add tests to check for presence of main content ID element
    # - add tests to check for all css/js/png/jpg/jpeg/svg present being reachable
    


