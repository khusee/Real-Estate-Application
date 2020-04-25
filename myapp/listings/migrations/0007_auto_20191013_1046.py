# Generated by Django 2.2.6 on 2019-10-13 05:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20191013_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='floors',
            field=models.DecimalField(blank=True, decimal_places=1, default=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 13, 10, 46, 54, 551468)),
        ),
    ]
