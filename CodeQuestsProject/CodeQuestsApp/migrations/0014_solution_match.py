# Generated by Django 4.2.1 on 2023-07-14 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CodeQuestsApp', '0013_remove_solution_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CodeQuestsApp.match'),
        ),
    ]