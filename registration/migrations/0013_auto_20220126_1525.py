# Generated by Django 3.2.11 on 2022-01-26 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_profile_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='adventure',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='culture',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='history',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='sightseeing',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='wildlife',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profileimages'),
        ),
    ]
