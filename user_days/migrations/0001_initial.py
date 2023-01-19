# Generated by Django 4.1.5 on 2023-01-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('day_logged', models.DateField(blank=True)),
                ('foods_consumed', models.CharField(max_length=50)),
            ],
        ),
    ]
