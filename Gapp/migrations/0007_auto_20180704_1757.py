# Generated by Django 2.0.6 on 2018-07-04 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gapp', '0006_announcements_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcements',
            name='user',
        ),
        migrations.AlterField(
            model_name='announcements',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]