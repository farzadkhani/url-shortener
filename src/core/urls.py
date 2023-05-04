from django.contrib import admin
from django.urls import path, include

from redirect_apps.views import redirec_url_from_shortened_link_view

urlpatterns = [
    # admin URLs
    path("admin/", admin.site.urls),
    # includes
    path("redirect_apps/", include("redirect_apps.urls")),
    # redirect URL
    # !!! attenction: this url should be at the end of the urlpatherns
    path(
        "<str:short_code>/",
        redirec_url_from_shortened_link_view,
        name="redirec_url_for_shortened_link",
    ),
]
