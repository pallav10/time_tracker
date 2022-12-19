# -*- coding: utf-8 -*-

from datetime import datetime

from django.utils import timezone


def datetime_now() -> datetime:
    return timezone.now().replace(microsecond=0)


def today() -> datetime:
    return timezone.get_default_timezone().normalize(timezone.now()).date()
