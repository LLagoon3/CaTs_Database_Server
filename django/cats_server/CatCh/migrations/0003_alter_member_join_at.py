# Generated by Django 3.2.25 on 2024-07-10 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CatCh', '0002_rename_name_member_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='join_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
