from django.conf import settings # import the settings file

def tracking(request):
    if hasattr(settings, 'TRACKING_ENABLED'):
        return {'tracking_enabled': settings.TRACKING_ENABLED,
                'tracking_account': settings.TRACKING_ACCOUNT}
    else:
        return {'tracking_enabled': False,
                'tracking_account': ""}