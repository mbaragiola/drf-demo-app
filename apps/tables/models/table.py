from django.db import models


class Table(models.Model):
    table_name = models.CharField(max_length=100, unique=True, db_index=True)
    fields = models.JSONField()

    class Meta:
        verbose_name = 'table'
        verbose_name_plural = 'tables'
        ordering = ['table_name']
