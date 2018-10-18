from django.contrib import admin

from .models import  JobsModel
# Register your models here.
class JobsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'kind','done','working')

admin.site.register(JobsModel,JobsAdmin)
