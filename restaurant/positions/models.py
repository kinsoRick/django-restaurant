from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from PIL import Image


class Tip(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя человека")
    card_number = models.CharField(max_length=30, blank=True, null=True, verbose_name="Номер карты")
    payment_link = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на оплату")
    photo = models.ImageField(upload_to="tip_photos/", blank=True, null=True, verbose_name="Фотография")

    class Meta:
        verbose_name = _("Чаевые")
        verbose_name_plural = _("Чаевые")
        constraints = [
            models.CheckConstraint(
                check=models.Q(card_number__isnull=False) | models.Q(payment_link__isnull=False),
                name="one_of_card_number_or_payment_link_required",
            )
        ]

    def __str__(self):
        return self.name


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    image = models.ImageField(upload_to="category_images/", null=True, blank=True, verbose_name="Изображение")
    url = models.CharField(max_length=100, default="/", verbose_name="Не прямая ссылка")
    priority = models.IntegerField(default=0, verbose_name="Приоритет")

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")

    def __str__(self):
        return self.name


@receiver(post_save, sender=Category)
def resize_category_image(sender, instance, **kwargs):
    if instance.image:
        img = Image.open(instance.image.path)
        img.thumbnail((640, 640))
        img.save(instance.image.path)


class SubCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    priority = models.IntegerField(default=0, verbose_name="Приоритет")

    class Meta:
        verbose_name = _("Подкатегория")
        verbose_name_plural = _("Подкатегории")

    def __str__(self):
        return self.name


class Position(models.Model):
    SPICY_LEVEL_CHOICES = [
        ("Не острая", "Не острая"),
        ("Незначительно", "Незначительно"),
        ("Средне", "Средне"),
        ("Острое", "Острое"),
        ("Очень острое", "Очень острое"),
    ]
    name = models.CharField(max_length=100, verbose_name="Имя")
    image = models.ImageField(upload_to="positions/", null=True, blank=True, verbose_name="Изображение")
    description = models.TextField(default="", blank=True, null=True, verbose_name="Описание")

    price = models.CharField(default="", blank=True, null=True, verbose_name="Цена (в рублях)")
    weight = models.CharField(default="", blank=True, null=True, verbose_name="Вес и измерения")

    cooking_time = models.PositiveIntegerField(default=0, verbose_name="Время готовки (в минутах)")
    is_new = models.BooleanField(default=True, verbose_name="Позиция новая?")

    spiciness = models.CharField(
        max_length=20,
        choices=SPICY_LEVEL_CHOICES,
        default="Не острая",
        verbose_name="Острота",
    )

    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name="Подкатегория")
    priority = models.PositiveIntegerField(default=0, verbose_name="Приоритет")

    is_active = models.BooleanField(default=True, verbose_name="Позиция активна?")

    class Meta:
        verbose_name = _("Позиция")
        verbose_name_plural = _("Позиции")

    def __str__(self):
        return self.name


@receiver(post_save, sender=Position)
def resize_position_image(sender, instance, **kwargs):
    if instance.image:
        img = Image.open(instance.image.path)
        img.thumbnail((640, 640))
        img.save(instance.image.path)
