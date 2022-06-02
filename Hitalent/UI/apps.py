from django.apps import AppConfig


class UiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UI'
    def ready(self):
        import UI.signals