__author__ = 'stefan'

from catalog.models import Category
import settings

def estore(request):
    return {
        'site_name': settings.SITE_NAME,
        'meta_keywords': settings.META_KEYWORDS,
        'meta_description': settings.META_DESCRIPTION,
        'request': request
    }