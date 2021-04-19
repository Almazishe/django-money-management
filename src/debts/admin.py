from django.contrib import admin

from .models import OperationCategory, Operation



admin.site.register(Operation)
admin.site.register(OperationCategory)
