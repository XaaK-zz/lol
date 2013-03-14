from django.conf import settings # import the settings file
from lol.models import Snippet, Language

def tracking(request):
    if hasattr(settings, 'TRACKING_ENABLED'):
        return {'tracking_enabled': settings.TRACKING_ENABLED,
                'tracking_account': settings.TRACKING_ACCOUNT}
    else:
        return {'tracking_enabled': False,
                'tracking_account': ""}
         
def languages(request):
    return {'languages': Language.objects.filter(active=True).extra(select={'lower_name': 'lower(name)'}).order_by('lower_name') }