# Generated by Django 5.1.2 on 2024-10-15 15:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_remove_friends_dob_remove_friends_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("speed", models.IntegerField()),
            ],
        ),
    ]
