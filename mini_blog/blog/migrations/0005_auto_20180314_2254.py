# Generated by Django 2.0.2 on 2018-03-14 21:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180314_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.TimeField(default=datetime.datetime(2018, 3, 14, 21, 54, 53, 590867, tzinfo=utc)),
        ),
    ]