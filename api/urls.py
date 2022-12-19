"""
author :
date :
purpose :
"""

# future

# standard-library

# third-party
from django.urls import path
from rest_framework.routers import SimpleRouter

# django

# local
from api.views import TimeLogViewSet

urlpatterns = [
    path(
        'time-logs',
        TimeLogViewSet.as_view({"get": "list", "post": "create"}),
        name="logs",
    ),
    path(
        'time-logs/<int:pk>/',
        TimeLogViewSet.as_view(
            {
                "patch": "partial_update",
                "get": "retrieve",
                "delete": "destroy",
            }
        ),
        name="time-log",
    ),
]
