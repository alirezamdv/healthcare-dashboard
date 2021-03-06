# Generated by Django 3.0.10 on 2021-08-15 19:38

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthCareWorkers', '0004_auto_20210731_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='tasks',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='category',
            field=models.CharField(blank=True, choices=[('home', 'home'), ('school', 'school'), ('work', 'work'), ('others', 'others'), (None, 'null')], default='home', max_length=240, null=True),
        ),
    ]
