from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
      list_display = ("title", "description", "startTime",  "endTime", "completed", "created_on", "updated_on")

admin.site.register(Task, TaskAdmin)