from django.contrib import admin
from .models import QuestionsForRecruitment, FormResponses
from import_export.admin import ImportExportModelAdmin
from import_export import resources


## Question For Recruitment
class QuestionsForRecruitmentResource(resources.ModelResource):
    class Meta:
        model = QuestionsForRecruitment

## For Import export in the admin panel
class QuestionsForRecruitmentAdmin(ImportExportModelAdmin):
    resource_class = QuestionsForRecruitmentResource
    

admin.site.register(QuestionsForRecruitment,QuestionsForRecruitmentAdmin)



## Form Responses
class FormResponsesResource(resources.ModelResource):
    class Meta:
        model = FormResponses

class FormResponsesAdmin(ImportExportModelAdmin):
    resource_class = FormResponsesResource
    

admin.site.register(FormResponses,FormResponsesAdmin)