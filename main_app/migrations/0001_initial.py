# Generated by Django 4.2.13 on 2024-05-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('age', models.IntegerField()),
            ],
        ),
    ]