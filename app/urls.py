from django.urls import path
from app.views import (
    NewsListView,
    NewsCreateView,
    NewsUpdateView,
    NewsDeleteView
)


urlpatterns = [
    path("", NewsListView.as_view(), name="read_news"),
    path("create/", NewsCreateView.as_view(), name="create_news"),
    path("<int:pk>/update/", NewsUpdateView.as_view(), name="update_news"),
    path("<int:pk>/delete/", NewsDeleteView.as_view(), name="delete_news"),
]
