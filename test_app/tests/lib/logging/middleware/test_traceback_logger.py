import mock
from django.test import TestCase

from ansible_base.lib.middleware.logging.log_request import LogTracebackMiddleware


class TestLogTracebackMiddleware(TestCase):
    def test_log_traceback_middleware(self):
        get_response = mock.MagicMock()
        request = self.factory.get('/')

        middleware = LogTracebackMiddleware(get_response)
        response = middleware(request)

        # ensure get_response has been returned
        self.assertEqual(get_response.return_value, response)

        # pretend we've been sent a signal and call handle_signal method
        with self.assertLogs(logger='ansible_base.lib.middleware.logging.log_request', level='ERROR') as captured_log:
            middleware.handle_signal()
            self.assertIn("traceback", captured_log.output)
