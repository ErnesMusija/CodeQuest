# Generated by Django 4.2 on 2023-05-05 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeQuestsApp', '0006_solution_passed_usercourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='queued',
            field=models.BooleanField(default=True),
        ),
    ]
