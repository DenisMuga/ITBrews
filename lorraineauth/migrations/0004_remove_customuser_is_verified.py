# Generated by Django 4.0.5 on 2022-06-23 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lorraineauth', '0003_alter_customuser_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_verified',
        ),
    ]
