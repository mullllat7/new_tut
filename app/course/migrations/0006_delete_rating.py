# Generated by Django 4.0 on 2022-04-16 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_rename_pin_rating_course'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]