# Generated by Django 4.2.9 on 2024-02-11 22:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("positions", "0008_alter_position_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="position",
            name="is_liquid",
            field=models.BooleanField(default=False),
        ),
    ]