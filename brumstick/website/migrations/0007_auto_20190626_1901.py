# Generated by Django 2.2.2 on 2019-06-26 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20190626_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='<int:pk>'),
        ),
    ]
