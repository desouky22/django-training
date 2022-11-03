# Generated by Django 4.1.3 on 2022-11-03 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("artists", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Album",
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
                ("name", models.CharField(default="New Album", max_length=100)),
                ("creation_datetime", models.DateTimeField(auto_now_add=True)),
                ("release_datetime", models.DateTimeField()),
                ("cost", models.DecimalField(decimal_places=2, max_digits=9)),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="artists.artist"
                    ),
                ),
            ],
        ),
    ]
