# Generated by Django 3.2.9 on 2021-12-01 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20211127_1034'),
        ('course', '0020_tabooword'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enroll_requests', to='course.class')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.semester')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enroll_requests', to='accounts.profile')),
            ],
        ),
    ]
