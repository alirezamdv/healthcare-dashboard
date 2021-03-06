# Generated by Django 3.0.10 on 2021-07-31 08:49

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20210628_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='dengue',
            name='menstrual_bleeding',
            field=models.CharField(blank=True, choices=[('Positive', 'Positive'), ('Negative', 'Negative'), (None, 'null')], default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='admission_number',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=240, null=True, validators=[django.core.validators.RegexValidator('^[A][N]\\S{5}[/]\\d{4}', 'Only ANxxxxx/YY pattern is allowed.')]), null=True, size=None),
        ),
        migrations.AddField(
            model_name='patient',
            name='hospital_number',
            field=models.CharField(blank=True, max_length=240, null=True, validators=[django.core.validators.RegexValidator('^[H][N]\\S{5}[/]\\d{4}', 'Only HNxxxxx/YY pattern is allowed.')]),
        ),
        migrations.AlterField(
            model_name='dengue',
            name='eschar',
            field=models.CharField(blank=True, choices=[('Positive', 'Positive'), ('Negative', 'Negative'), (None, 'null')], default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='dengue',
            name='outcomeRl',
            field=models.CharField(blank=True, choices=[('Positive', 'Positive'), ('Negative', 'Negative'), (None, 'null')], default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='dengue',
            name='sensitivityAnalysis',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='admission_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
