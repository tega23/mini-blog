# Generated by Django 2.0.3 on 2018-03-15 08:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180315_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
