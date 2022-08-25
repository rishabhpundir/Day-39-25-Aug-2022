from django.apps import AppConfig


class RelappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relapp'

    def ready(self):
        import relapp.signals