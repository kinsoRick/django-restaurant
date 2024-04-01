from rest_framework import serializers

from restaurant.positions.models import Category, Position, SubCategory, Tip


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ["id", "name", "card_number", "payment_link", "photo"]


class PositionSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Position
        fields = [
            "id",
            "name",
            "description",
            "image",
            "price",
            "weight",
            "cooking_time",
            "spiciness",
            "is_new",
            "subcategory",
            "url",
            "is_active",
        ]

    def get_url(self, obj: Position):
        return f"{obj.subcategory.category.url}#position-{obj.id}"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"
