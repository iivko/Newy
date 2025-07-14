from django.contrib import admin
from django.urls import path, include

from allauth.account.views import SignupView
from django.views.generic import RedirectView
from django.conf import settings

"""
    Main Routes
"""
urlpatterns = [
    path(f"{settings.ADMIN_URL}", admin.site.urls),
    path("news/", include("app.urls")),
    path("", SignupView.as_view(), name="account_signup"),
    path("account/signup/", RedirectView.as_view(url="/")),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        path("__reload__/", include("django_browser_reload.urls")),
    ]
