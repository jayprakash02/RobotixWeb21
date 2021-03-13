from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import Event, Workshop

# Register your models here.

@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    pass

@admin.register(Workshop)
class WorkshopAdmin(ImportExportModelAdmin):
    pass
    
