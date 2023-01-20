# Generated by Django 4.1.5 on 2023-01-19 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='colors.color')),
            ],
        ),
    ]
