# Generated by Django 2.2.6 on 2019-10-21 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20191013_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 21, 14, 7, 38, 224120)),
        ),
    ]
