# Generated by Django 2.2.6 on 2019-10-21 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0011_auto_20191021_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 21, 15, 0, 54, 96968)),
        ),
    ]
