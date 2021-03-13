from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import UserProfile

# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(ImportExportModelAdmin):
    pass
