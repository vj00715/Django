# Generated by Django 4.1.2 on 2022-10-10 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_studentsignup_username_alter_studentsignup_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsignup',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]