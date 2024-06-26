# Generated by Django 4.1.13 on 2024-04-09 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="JournalProfile",
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
                ("name", models.CharField(max_length=100, verbose_name="Journal Name")),
                ("ranking", models.IntegerField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("O", "Open"), ("C", "Closed")],
                        default="C",
                        max_length=10,
                        null=True,
                        verbose_name="Submission status",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=200, null=True, verbose_name="Email"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Journal description"
                    ),
                ),
                (
                    "submission_criteria",
                    models.TextField(
                        blank=True, null=True, verbose_name="Submission criteria"
                    ),
                ),
                (
                    "journal_cover",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="",
                        verbose_name="Journal Cover Picture",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-ranking"],
            },
        ),
        migrations.AddIndex(
            model_name="journalprofile",
            index=models.Index(
                fields=["-ranking"], name="journal_jou_ranking_d32394_idx"
            ),
        ),
    ]
