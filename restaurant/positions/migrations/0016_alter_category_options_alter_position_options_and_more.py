# Generated by Django 4.2.9 on 2024-02-12 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("positions", "0015_remove_position_measurement_alter_position_price_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории"},
        ),
        migrations.AlterModelOptions(
            name="position",
            options={"verbose_name": "Позиция", "verbose_name_plural": "Позиции"},
        ),
        migrations.AlterModelOptions(
            name="subcategory",
            options={
                "verbose_name": "Подкатегория",
                "verbose_name_plural": "Подкатегории",
            },
        ),
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="category_images/",
                verbose_name="Изображение",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="category",
            name="priority",
            field=models.IntegerField(default=0, verbose_name="Приоритет"),
        ),
        migrations.AlterField(
            model_name="category",
            name="url",
            field=models.CharField(
                default="/", max_length=100, verbose_name="Не прямая ссылка"
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="cooking_time",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Время готовки (в минутах)"
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="description",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="positions/",
                verbose_name="Изображение",
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="is_new",
            field=models.BooleanField(default=True, verbose_name="Позиция новая?"),
        ),
        migrations.AlterField(
            model_name="position",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="position",
            name="price",
            field=models.CharField(
                blank=True, default="", null=True, verbose_name="Цена (в рублях)"
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="priority",
            field=models.IntegerField(default=0, verbose_name="Приоритет"),
        ),
        migrations.AlterField(
            model_name="position",
            name="subcategory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="positions.subcategory",
                verbose_name="Подкатегория",
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="weight",
            field=models.CharField(
                blank=True, default="", null=True, verbose_name="Вес и измерения"
            ),
        ),
        migrations.AlterField(
            model_name="subcategory",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="positions.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="subcategory",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="subcategory",
            name="priority",
            field=models.IntegerField(default=0, verbose_name="Приоритет"),
        ),
    ]
