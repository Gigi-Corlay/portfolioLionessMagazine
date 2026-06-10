from django.test import TestCase


class AuthenticationTest(TestCase):

    def test_dashboard_requires_login(self):

        response = self.client.get("/dashboard/")

        self.assertEqual(
            response.status_code,
            302
        )
