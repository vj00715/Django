# Generated by Django 4.1.2 on 2022-10-13 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_result_rename_totalmarks_courses_questionmarks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='marks',
        ),
    ]