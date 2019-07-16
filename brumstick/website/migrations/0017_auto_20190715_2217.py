# Generated by Django 2.2.2 on 2019-07-15 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20190715_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='part1_content',
            new_name='part10_link',
        ),
        migrations.RenameField(
            model_name='projects',
            old_name='part2_content',
            new_name='part1_link',
        ),
        migrations.RenameField(
            model_name='projects',
            old_name='part3_content',
            new_name='part2_link',
        ),
        migrations.AddField(
            model_name='projects',
            name='part3_link',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='part4_link',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='part5_link',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='part6_link',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='part7_link',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='part8_link',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='part9_link',
            field=models.TextField(blank=True),
        ),
    ]