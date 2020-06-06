from django.db import models


class Entry(models.Model):
    table = models.ForeignKey('tables.Table', on_delete=models.CASCADE)
    data = models.JSONField()

    class Meta:
        verbose_name = 'entry'
        verbose_name_plural = 'entries'
        ordering = ['table_name']
