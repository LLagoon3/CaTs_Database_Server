# Generated by Django 3.2.25 on 2024-07-10 01:09

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('login_id', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=40)),
                ('join_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LoverRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField()),
                ('member_id1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lover_relationships_1', to='CatCh.member')),
                ('member_id2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lover_relationships_2', to='CatCh.member')),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('letter_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_path', models.CharField(max_length=255)),
                ('sent_at', models.DateField()),
                ('receiver_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='received_letters', to='CatCh.member')),
                ('sender_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sent_letters', to='CatCh.member')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField()),
                ('member_id1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_relationships_1', to='CatCh.member')),
                ('member_id2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_relationships_2', to='CatCh.member')),
            ],
        ),
        migrations.AddConstraint(
            model_name='loverrelationship',
            constraint=models.UniqueConstraint(fields=('member_id1', 'member_id2'), name='unique_lover_relationships'),
        ),
        migrations.AddConstraint(
            model_name='loverrelationship',
            constraint=models.CheckConstraint(check=models.Q(('member_id1', django.db.models.expressions.F('member_id2')), _negated=True), name='check_lover_different_members'),
        ),
        migrations.AddConstraint(
            model_name='familyrelationship',
            constraint=models.UniqueConstraint(fields=('member_id1', 'member_id2'), name='unique_family_relationships'),
        ),
        migrations.AddConstraint(
            model_name='familyrelationship',
            constraint=models.CheckConstraint(check=models.Q(('member_id1', django.db.models.expressions.F('member_id2')), _negated=True), name='check_family_different_members'),
        ),
    ]
