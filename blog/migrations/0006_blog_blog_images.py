# Generated by Django 3.2.10 on 2022-02-13 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_images',
            field=models.FileField(blank=True, null=True, upload_to='blogimages'),
        ),
    ]
