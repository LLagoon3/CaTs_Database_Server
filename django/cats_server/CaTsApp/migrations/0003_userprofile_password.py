# Generated by Django 3.2.25 on 2024-03-27 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CaTsApp', '0002_auto_20240326_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Password',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
