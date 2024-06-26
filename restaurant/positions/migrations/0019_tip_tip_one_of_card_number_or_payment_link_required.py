# Generated by Django 4.2.9 on 2024-02-14 19:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("positions", "0018_alter_position_priority"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tip",
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
                ("name", models.CharField(max_length=100, verbose_name="Имя человека")),
                (
                    "card_number",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="Номер карты"
                    ),
                ),
                (
                    "payment_link",
                    models.URLField(
                        blank=True, null=True, verbose_name="Ссылка на оплату"
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="tip_photos/",
                        verbose_name="Фотография",
                    ),
                ),
            ],
            options={
                "verbose_name": "Чаевые",
                "verbose_name_plural": "Чаевые",
            },
        ),
        migrations.AddConstraint(
            model_name="tip",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("card_number__isnull", False),
                    ("payment_link__isnull", False),
                    _connector="OR",
                ),
                name="one_of_card_number_or_payment_link_required",
            ),
        ),
    ]
