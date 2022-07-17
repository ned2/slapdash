import subprocess
import sys
from importlib import import_module, invalidate_caches

import dash
import pytest


def install_package(package):
    """Install the supplied package into the current environment."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def bake_install_and_get_app_module(cookies, project_name="test_app"):
    """Bake the recipe, install the package, and return the `index` module"""
    result = cookies.bake(extra_context={"project_name": project_name})
    install_package(result.project_path)
    invalidate_caches()
    app_module = import_module(".app", package=project_name)
    return app_module


def test_bake_project(cookies, project_name="test_app"):
    """Test that the cookiecutter recipe is baked."""
    result = cookies.bake(extra_context={"project_name": project_name})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()
    assert result.project_path.name == project_name


def test_baked_app_routes(cookies, dash_thread_server):
    """Test that app in the baked project runs and all routes are accessible."""
    app_module = bake_install_and_get_app_module(cookies)
    app = app_module.app
    dash_thread_server.start(app_module.app)

    for page in dash.page_registry.values():
        url = f"{dash_thread_server.url}/{page['path']}"
        assert dash_thread_server.accessible(url), f"Loading route '{url}' failed"
    css_url = f"{dash_thread_server.url}/assets/app.css"    
    assert dash_thread_server.accessible(url), f"Loading route '{css_url}' failed"

    
@pytest.mark.webdriver
def test_baked_app_frontend(cookies, dash_duo):
    """Test that the Dash app in the baked project runs."""
    app_module = bake_install_and_get_app_module(cookies)
    dash_duo.start_server(app_module.app)

    dash_duo.wait_for_element_by_id(dash.dash._ID_CONTENT)

