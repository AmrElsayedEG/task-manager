from django.contrib import admin

# Register your models here.
from task.models import task

admin.site.register(task)