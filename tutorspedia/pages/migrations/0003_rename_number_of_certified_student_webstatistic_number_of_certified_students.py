# Generated by Django 4.1.1 on 2022-10-11 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_availablecourse_expertinstructor_webstatistic_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webstatistic',
            old_name='number_of_certified_student',
            new_name='number_of_certified_students',
        ),
    ]
