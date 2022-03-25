from django.apps import AppConfig


class UiConfig(AppConfig):
    default_auto_feild='django.db.models.BigAutoFeild'
    
    name = 'UI'
    def ready(self):
        import UI.signals