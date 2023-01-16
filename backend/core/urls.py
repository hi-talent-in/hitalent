from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("intern/", include("ht_intern.urls")),
    # path("a/", include("allauth.urls")),
]
