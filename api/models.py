from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class TimeStampModelMixin(models.Model):
    """
    Adds created_at and last_modified for timestamp change tracking.
    """

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    last_modified = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class Project(TimeStampModelMixin):
    name = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TimeLog(TimeStampModelMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='logs',
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='user_logs',
        blank=True,
        null=True,
    )
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    details = models.CharField(max_length=256, default='', null=True, blank=True)

    def __str__(self):
        return f"hours: {self.time_diff_in_hours} - details: {self.details}"

    class Meta:
        verbose_name = 'time log'
        verbose_name_plural = "time logs"

    @property
    def time_diff_in_hours(self):
        if self.end_time and self.start_time:
            seconds = (self.end_time - self.start_time).total_seconds()
            return seconds / 3600
        return 0
