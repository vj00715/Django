# Generated by Django 4.1.2 on 2022-10-14 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_alter_question_coursequestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='studentMarks',
            field=models.FloatField(null=True),
        ),
    ]
