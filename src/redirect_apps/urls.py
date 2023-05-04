from django.urls import path

from .views import CreateShortenedLinkCreateView


urlpatterns = [
    # url for create new shortened link and have short_code in query string
    path(
        "create_shortened_link/<str:short_code>/",
        CreateShortenedLinkCreateView.as_view(),
        name="have-shortened-link",
    ),
]
