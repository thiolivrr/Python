# Generated by Django 5.0.1 on 2024-01-20 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal_app.meal')),
            ],
            options={
                'verbose_name_plural': 'descriptions',
            },
        ),
    ]
