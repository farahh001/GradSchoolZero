# Generated by Django 3.2.9 on 2021-11-23 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='first_name',
            field=models.CharField(default=' ', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='last_name',
            field=models.CharField(default=' ', max_length=150),
            preserve_default=False,
        ),
    ]
