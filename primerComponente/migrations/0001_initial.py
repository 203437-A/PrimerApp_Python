# Generated by Django 4.0.1 on 2022-01-17 07:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrimerModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo_uno', models.CharField(max_length=255, null=True)),
                ('edad', models.IntegerField(default=0, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('edit', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
    ]
