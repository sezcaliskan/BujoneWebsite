from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(JournalModel)
admin.site.register(Todo)
admin.site.register(Idea)
