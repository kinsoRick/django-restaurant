# Generated by Django 4.2.9 on 2024-02-11 23:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("positions", "0012_alter_position_measurement_alter_position_spiciness"),
    ]

    operations = [
        migrations.AlterField(
            model_name="position",
            name="measurement",
            field=models.CharField(
                default="гр", max_length=20, verbose_name="Измерение"
            ),
        ),
    ]
