from django.contrib import admin
from django.urls import path, include


"""
    Main Routes
"""
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
]
