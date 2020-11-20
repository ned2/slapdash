def test_bake_project(cookies):
    """Test that the cookiecutter recipe is baked."""
    project_slug = "my_app"
    result = cookies.bake(extra_context={"project_slug": project_slug})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.isdir()
    assert result.project.basename == project_slug
