# Generated by Django 2.2.6 on 2019-10-13 05:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0007_auto_20191013_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 13, 11, 22, 30, 59638)),
        ),
    ]
