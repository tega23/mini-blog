# Generated by Django 2.0.2 on 2018-03-14 21:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180314_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.TimeField(default=datetime.datetime(2018, 3, 14, 22, 51, 53, 968253)),
        ),
    ]