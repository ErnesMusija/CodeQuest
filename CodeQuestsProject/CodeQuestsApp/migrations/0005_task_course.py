# Generated by Django 4.2 on 2023-05-01 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CodeQuestsApp', '0004_table_alter_task_difficulty_level_ranking'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CodeQuestsApp.course'),
        ),
    ]
