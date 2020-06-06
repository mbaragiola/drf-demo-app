from django.contrib.postgres.fields import JSONField
from django.db import models


class Table(models.Model):
    table_name = models.SlugField(unique=True, db_index=True)
    fields = JSONField()

    class Meta:
        verbose_name = 'table'
        verbose_name_plural = 'tables'
        ordering = ['table_name']
