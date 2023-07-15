from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    # name = 'full.python.path.to.your.app.companies'
    # label = 'my.companies'  # <-- this is the important line - change it to anything other than the default, which is the module name ('acount' in this case)
    default_auto_field = 'django.db.models.BigAutoField'
    name = "companies"
