# Generated by Django 4.1.2 on 2022-10-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0009_remove_teachersignup_activeteacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachersignup',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
