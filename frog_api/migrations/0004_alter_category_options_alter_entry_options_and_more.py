# Generated by Django 4.1 on 2022-08-22 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "frog_api",
            "0003_rename_decompiled_functions_entry_decompiled_chunks_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="entry",
            options={"ordering": ["-timestamp"], "verbose_name_plural": "Entries"},
        ),
        migrations.AlterField(
            model_name="version",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="versions",
                to="frog_api.project",
            ),
        ),
        migrations.CreateModel(
            name="Measure",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                ("type", models.CharField(max_length=255)),
                ("value", models.IntegerField()),
                (
                    "entry",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="measures",
                        to="frog_api.entry",
                    ),
                ),
            ],
        ),
    ]
