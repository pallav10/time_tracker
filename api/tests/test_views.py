from datetime import timedelta

# Create your tests here.
from model_bakery import baker
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from api.models import *

# Create your tests here.
from common.utils.date import datetime_now


class TestSubscriptionApi(APITestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        self.user = baker.make(settings.AUTH_USER_MODEL)
        baker.make(Token, user=self.user)
        self.time_log = baker.make(
            TimeLog,
            user=self.user,
            start_time=datetime_now() - timedelta(hours=6),
            end_time=datetime_now(),
        )
        other_logs = baker.make(TimeLog, _quantity=10)
        self.invalid_update_log = other_logs[0]
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.user.auth_token}")

    def test_get_all_time_logs(self):
        response = self.client.get(
            path=reverse("logs"),
        )
        self.assertEqual(response.status_code, 200)

    def test_create_time_log(self):
        response = self.client.post(
            path=reverse("logs"),
            data={
                'start_time': (datetime_now() - timedelta(hours=5)).strftime("%H:%M"),
                'end_time': datetime_now().time().strftime("%H:%M"),
            },
        )
        self.assertEqual(response.status_code, 201)

    def test_get_single_time_log(self):
        response = self.client.get(
            path=reverse(
                "time-log",
                (self.time_log.pk,),
            ),
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_single_time_log(self):
        response = self.client.delete(
            path=reverse(
                "time-log",
                (self.time_log.pk,),
            ),
        )
        self.assertEqual(response.status_code, 204)

    def test_patch_single_time_log(self):
        response = self.client.patch(
            path=reverse(
                "time-log",
                (self.time_log.pk,),
            ),
        )
        self.assertEqual(response.status_code, 200)

    def test_get_single_time_log_invalid(self):
        response = self.client.get(
            path=reverse(
                "time-log",
                (self.invalid_update_log.pk,),
            ),
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_single_time_log_invalid(self):
        response = self.client.delete(
            path=reverse(
                "time-log",
                (self.invalid_update_log.pk,),
            ),
        )
        self.assertEqual(response.status_code, 404)

    def test_patch_single_time_log_invalid(self):
        response = self.client.patch(
            path=reverse(
                "time-log",
                (self.invalid_update_log.pk,),
            ),
        )
        self.assertEqual(response.status_code, 404)
