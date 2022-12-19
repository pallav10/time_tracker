from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import TimeLog, Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProjectSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class SideEffectsEvaluationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLog
        fields = "__all__"


class TimeLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    project_id = serializers.PrimaryKeyRelatedField(
        source='project', queryset=Project.objects.all(), write_only=True
    )
    project = ProjectSerializer(read_only=True)

    mandatory_project_validation_methods = ('post', 'delete')

    class Meta:
        model = TimeLog
        fields = "__all__"

    def validate(self, attrs):
        request = self.context['request']
        method = request.method.lower()
        user = request.user
        project = attrs.get('project')
        if (
            method in self.mandatory_project_validation_methods
            and not project.members.filter(pk=user.pk).exists()
        ):
            raise serializers.ValidationError("user does not belong to project")
        return attrs
