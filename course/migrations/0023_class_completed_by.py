# Generated by Django 3.2.9 on 2021-12-01 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20211127_1034'),
        ('course', '0022_labelofhonor'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='completed_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='completed_classes', to='accounts.Profile'),
        ),
    ]
