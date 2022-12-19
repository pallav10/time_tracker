from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated


# Create your views here.
from rest_framework.response import Response

from api.models import (
    TimeLog,
)
from api.serializers import TimeLogSerializer

import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)


class TimeLogViewSet(viewsets.ModelViewSet):
    """
    A view-set for viewing and editing time log instances.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = TimeLogSerializer
    queryset = TimeLog.objects.all()

    def get_object(self):
        obj = get_object_or_404(
            self.queryset, user=self.request.user, pk=self.kwargs.get('pk')
        )
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
