# Generated by Django 3.2.25 on 2024-07-10 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CatCh', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='name',
            new_name='user_name',
        ),
    ]