# Generated by Django 3.2.25 on 2024-03-21 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_auto_20240321_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approveduser',
            old_name='approveduser_student_id',
            new_name='student_id',
        ),
        migrations.RenameField(
            model_name='attendancelist',
            old_name='attendancelist_student_id',
            new_name='student_id',
        ),
    ]
