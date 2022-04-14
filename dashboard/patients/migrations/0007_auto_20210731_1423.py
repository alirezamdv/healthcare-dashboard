# Generated by Django 3.0.10 on 2021-07-31 14:23

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_auto_20210731_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='admission_number',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=240, null=True, validators=[django.core.validators.RegexValidator('^[A][N]\\S{5}[/]\\d{2}', 'Only ANxxxxx/YY pattern is allowed.')]), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='patient',
            name='hospital_number',
            field=models.CharField(blank=True, max_length=240, null=True, validators=[django.core.validators.RegexValidator('^[H][N]\\S{5}[/]\\d{2}', 'Only HNxxxxx/YY pattern is allowed.')]),
        ),
    ]
