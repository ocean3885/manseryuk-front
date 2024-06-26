# Generated by Django 5.0.6 on 2024-05-30 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('data', models.JSONField(blank=True, default=dict)),
                ('gen', models.CharField(blank=True, max_length=1)),
                ('sl', models.CharField(blank=True, max_length=10)),
                ('year', models.CharField(blank=True, max_length=4)),
                ('month', models.CharField(blank=True, max_length=2)),
                ('day', models.CharField(blank=True, max_length=2)),
                ('hour', models.CharField(blank=True, max_length=2)),
                ('min', models.CharField(blank=True, max_length=2)),
            ],
        ),
    ]
