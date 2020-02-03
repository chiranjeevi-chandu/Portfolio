from django.conf import settings


def add_variable_to_context(request):
    return {
        'BG_STYLE': settings.BG_STYLE
    }