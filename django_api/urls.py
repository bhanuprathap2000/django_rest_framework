"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from test_app.views import TestView,TestGenricView,TestUpdateView #class based view 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', TestView.as_view()),#this is a class based view sp based on the type of request the corresponding handler method is called
    path('test/<int:id>', TestView.as_view()),
    path('test-generic/', TestGenricView.as_view()),#this class is inherting from generics class based view
    path('test-generic/<int:id>', TestUpdateView.as_view()),#this also inherits from generics class based view
]
#only for development purpose
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns