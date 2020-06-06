from django.contrib.postgres.fields import JSONField
from django.db import models


class Entry(models.Model):
    table = models.ForeignKey('tables.Table', on_delete=models.CASCADE)
    data = JSONField()

    class Meta:
        verbose_name = 'entry'
        verbose_name_plural = 'entries'
