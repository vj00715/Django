# Generated by Django 4.1.2 on 2022-10-14 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_remove_result_marks_result_studentmarks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]