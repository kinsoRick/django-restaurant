# Generated by Django 4.2.9 on 2024-02-12 22:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("positions", "0017_alter_position_spiciness"),
    ]

    operations = [
        migrations.AlterField(
            model_name="position",
            name="priority",
            field=models.PositiveIntegerField(default=0, verbose_name="Приоритет"),
        ),
    ]
