from django.contrib import admin

# Register your models here.
from .models import TestModel,ModelX

# Register your models here.so that they can be viewed in the admin page
admin.site.register((TestModel,ModelX))#in order to register multiple models we need to use a tuple and pass the models as a tuple