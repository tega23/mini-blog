# Generated by Django 2.0.3 on 2018-03-19 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20180319_0907'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['post_date']},
        ),
    ]
