# Generated by Django 4.1.2 on 2022-10-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_rename_questionnumber_courses_totalquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='totalMarks',
            new_name='questionMarks',
        ),
    ]
