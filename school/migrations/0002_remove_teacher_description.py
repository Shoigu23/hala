# Generated by Django 4.1.7 on 2023-02-23 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='description',
        ),
    ]
