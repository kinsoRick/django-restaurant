from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PositionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "restaurant.positions"
    verbose_name = _("Карточки позиций")
