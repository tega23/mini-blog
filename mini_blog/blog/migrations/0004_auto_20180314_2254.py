# Generated by Django 2.0.2 on 2018-03-14 21:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180314_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.TimeField(default=datetime.datetime(2018, 3, 14, 21, 54, 1, 36181, tzinfo=utc)),
        ),
    ]
