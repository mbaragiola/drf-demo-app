# Generated by Django 3.0.7 on 2020-06-06 14:57

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.SlugField(unique=True)),
                ('fields', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'verbose_name': 'table',
                'verbose_name_plural': 'tables',
                'ordering': ['table_name'],
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Table')),
            ],
            options={
                'verbose_name': 'entry',
                'verbose_name_plural': 'entries',
            },
        ),
    ]
