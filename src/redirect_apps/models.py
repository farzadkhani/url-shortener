from django.db import models

from main_app.mixins import ModelMixin

from .utils import create_6_character_code


# Create your models here.


class RedirectModel(ModelMixin):
    short_code = models.CharField(max_length=15, unique=True)
    url = models.URLField(max_length=200)
    visit_counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return super().__str__()

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = create_6_character_code(self)
        super().save(*args, **kwargs)
