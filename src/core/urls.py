from django.contrib import admin
from django.urls import path, include

from redirect_apps.views import (
    redirec_url_from_shortened_link_view,
    CreateShortenedLinkCreateView,
)


urlpatterns = [
    # admin URLs
    path("admin/", admin.site.urls),
    # includes
    path("redirect_apps/", include("redirect_apps.urls")),
    # home page.
    path(
        "",
        CreateShortenedLinkCreateView.as_view(),
        name="create-shortened-link",
    ),
    # redirect URL
    # !!! attenction: this url should be at the end of the urlpatherns
    path(
        "<str:short_code>/",
        redirec_url_from_shortened_link_view,
        name="redirec_url_for_shortened_link",
    ),
]
