# Generated by Django 3.2.25 on 2024-03-26 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0006_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]
