# Generated by Django 5.1.2 on 2024-10-19 13:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("recipe", "0002_remove_recipes_estimated_time_recipes_recipe_img"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipes",
            name="ingredients",
        ),
    ]
