import uuid
from django.db import models



class DateModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        null=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения',
        null=True,
    )

    class Meta:
        abstract = True
        ordering = ('-created_at', )

    def __str__(self) -> str:
        return str(self.created_at)