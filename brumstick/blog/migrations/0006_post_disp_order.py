# Generated by Django 2.2.2 on 2019-07-01 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190628_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='disp_order',
            field=models.IntegerField(blank=True, default=1000000),
        ),
    ]
