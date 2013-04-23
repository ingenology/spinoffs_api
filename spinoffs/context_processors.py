from django.conf import settings

def constants(request):
    """
    Adds selected constants to the context.
    """
    admin_page = True if request.path.startswith('/admin/') else False
    return {
        'PROJECT_NAME': getattr(settings, 'PROJECT_NAME', ''),
        'PROJECT_AUTHOR': getattr(settings, 'PROJECT_AUTHOR', ''),
        'admin_page': admin_page,
    }
