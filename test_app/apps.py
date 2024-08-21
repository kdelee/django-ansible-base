import signal

from django.apps import AppConfig

from ansible_base.lib.middleware.logging import LogTracebackMiddleware


class TestAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_app'

    def ready(self):
        super().ready()
        signal.signal(signal.SIGSYS, LogTracebackMiddleware.handle_signal)
