from django.contrib import admin
from main_app.mixins import ModelAdminMixin

from .models import RedirectModel


# Register your models here.
@admin.register(RedirectModel)
class RedirectModelModelAdmin(ModelAdminMixin):
    """
    implement admin for RedirectModel
    """

    list_display = [
        "id",
        "short_code",
        "url",
        "visit_counter",
        "is_active",
        "is_removed",
    ]

    list_filter = [
        "created_at",
        "updated_at",
        "short_code",
        "url",
        "visit_counter",
        "is_active",
        "is_removed",
    ]
