# Generated by Django 4.2.9 on 2024-02-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("positions", "0019_tip_tip_one_of_card_number_or_payment_link_required"),
    ]

    operations = [
        migrations.AddField(
            model_name="position",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Позиция активна?"),
        ),
    ]
