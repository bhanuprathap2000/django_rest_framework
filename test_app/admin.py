from django.contrib import admin

# Register your models here.
from .models import TestModel

# Register your models here.so that they can be viewed in the admin page
admin.site.register(TestModel)