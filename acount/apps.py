from django.apps import AppConfig


class AcountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'acount'
    # label = 'acount'  # <-- this is the important line - change it to anything other than the default, which is the module name ('acount' in this case)
