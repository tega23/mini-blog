# Generated by Django 2.0.2 on 2018-03-14 21:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateField(default=datetime.date(2018, 3, 14)),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_time',
            field=models.TimeField(default=datetime.datetime(2018, 3, 14, 22, 26, 26, 962693)),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='post_date',
            field=models.DateField(default=datetime.date(2018, 3, 14), null=True),
        ),
    ]