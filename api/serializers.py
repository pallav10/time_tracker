from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import TimeLog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class SideEffectsEvaluationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLog
        fields = "__all__"


class TimeLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = TimeLog
        fields = "__all__"
