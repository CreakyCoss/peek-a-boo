from . import main


@main.app_errorhandler(404)
def page_not_found():
    return '404 not found', 404
