# Generated by Django 2.2.2 on 2019-06-26 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_projects_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='image',
            new_name='main_image',
        ),
    ]