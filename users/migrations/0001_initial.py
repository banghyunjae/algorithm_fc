# Generated by Django 4.1.7 on 2023-05-12 08:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="email address"
                    ),
                ),
                ("name", models.CharField(default="test_user", max_length=100)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "male"),
                            ("female", "female"),
                            ("other", "other"),
                        ],
                        default="other",
                        max_length=6,
                    ),
                ),
                ("age", models.IntegerField(default=20, null=True)),
                ("introduction", models.TextField(default="소개글 입니다.", null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("image", models.ImageField(blank=True, upload_to="%Y/%m/%d/")),
                (
                    "followings",
                    models.ManyToManyField(
                        blank=True,
                        related_name="followers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
