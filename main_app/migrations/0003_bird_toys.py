# Generated by Django 4.2.13 on 2024-05-31 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_toy_feeding'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]
