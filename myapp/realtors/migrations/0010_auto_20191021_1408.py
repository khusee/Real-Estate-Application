# Generated by Django 2.2.6 on 2019-10-21 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0009_auto_20191021_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 21, 14, 8, 53, 390055)),
        ),
    ]
