# Generated by Django 2.2.2 on 2019-06-26 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_projects_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='images',
        ),
    ]
