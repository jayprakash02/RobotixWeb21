from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import *

# Register your models here.

@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(ImportExportModelAdmin):
    pass

@admin.register(CertImage)
class CertImageAdmin(ImportExportModelAdmin):
    pass