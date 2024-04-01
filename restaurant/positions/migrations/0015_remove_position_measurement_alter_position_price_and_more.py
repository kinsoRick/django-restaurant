# Generated by Django 4.2.9 on 2024-02-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("positions", "0014_alter_position_price_alter_position_weight"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="position",
            name="measurement",
        ),
        migrations.AlterField(
            model_name="position",
            name="price",
            field=models.CharField(blank=True, default="", null=True),
        ),
        migrations.AlterField(
            model_name="position",
            name="weight",
            field=models.CharField(blank=True, default="", null=True),
        ),
    ]
