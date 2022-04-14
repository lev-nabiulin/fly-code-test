from django.contrib import admin
from django.urls import path, include

from .views import BookListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('book.urls')),
    path("", BookListView.as_view()),
]