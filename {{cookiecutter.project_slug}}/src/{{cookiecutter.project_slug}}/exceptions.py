class {{ cookiecutter.project_slug.title() }}BaseException(Exception):
    pass


class InvalidLayoutError({{ cookiecutter.project_slug.title() }}BaseException):
    pass
