from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.admin.widgets import FilteredSelectMultiple

from api.models import TimeLog

admin.site.register(TimeLog, admin.ModelAdmin)
