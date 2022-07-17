from django.contrib import admin

# Register your models here.
from .models import Race, Training, Completed

admin.site.register(Race)
admin.site.register(Training)
admin.site.register(Completed)