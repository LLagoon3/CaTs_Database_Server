# Generated by Django 3.2.25 on 2024-03-20 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=1)),
                ('interest', models.TextField()),
                ('kakao_id', models.CharField(max_length=100)),
                ('motivation', models.TextField()),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('student_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('fcm_token', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ApprovedUser',
            fields=[
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='approved_users', serialize=False, to='Api.user')),
                ('gender', models.CharField(max_length=1)),
                ('interest', models.TextField()),
                ('kakao_id', models.CharField(max_length=100)),
                ('motivation', models.TextField()),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attedance_list', to='Api.user')),
            ],
        ),
    ]
