# Generated by Django 4.2.1 on 2023-05-25 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("frog_api", "0010_alter_entry_category_alter_project_discord_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="entry",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]
