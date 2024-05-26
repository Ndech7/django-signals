from django.apps import AppConfig


class SignalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signal_app'

    # register the signals in the application
    def ready(self):
        import signal_app.signals
