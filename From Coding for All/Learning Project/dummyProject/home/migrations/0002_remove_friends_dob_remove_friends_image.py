# Generated by Django 5.1.2 on 2024-10-15 09:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="friends",
            name="dob",
        ),
        migrations.RemoveField(
            model_name="friends",
            name="image",
        ),
    ]