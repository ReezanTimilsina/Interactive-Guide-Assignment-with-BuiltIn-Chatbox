# Generated by Django 3.2.7 on 2023-02-27 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0022_auto_20230227_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_guide',
        ),
    ]
