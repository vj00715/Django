# Generated by Django 4.1.2 on 2022-10-11 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_alter_teachersignup_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachersignup',
            name='foreign',
        ),
    ]