# Generated by Django 2.2.2 on 2019-06-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20190626_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='show_in_list',
            field=models.BooleanField(default=False),
        ),
    ]
