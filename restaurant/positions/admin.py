from django.contrib import admin

from .models import Category, Position, SubCategory, Tip


class PositionInline(admin.TabularInline):
    model = Position


class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    inlines = [PositionInline]


@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "photo", "payment_link"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline]
    search_fields = ["name"]
    list_display = ["name", "image", "url"]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    inlines = [PositionInline]
    search_fields = ["name"]
    list_display = ["name", "category"]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "subcategory", "price", "is_new"]
