from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Achievements

# Register your models here.

@admin.register(Achievements)
class AchievementsAdmin(ImportExportModelAdmin):
    pass
