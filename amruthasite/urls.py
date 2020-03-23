'''django2 version'''
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('amruthaweb/', include('amruthaweb.urls')),
    path('admin/', admin.site.urls),
]