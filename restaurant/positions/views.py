from django.shortcuts import get_object_or_404, render

from .models import Category, Position, Tip


def index(request):
    categories = Category.objects.all()

    return render(request, "positions/index.html", {"categories": categories})


def tips_list(request):
    tips = Tip.objects.all()

    return render(request, "positions/tips.html", {"tips": tips})


def category_detail(request, category_name):
    liked_positions = request.COOKIES.get("likedPositions")
    if not liked_positions:
        liked_positions = []
    category = get_object_or_404(Category, url=f"/{category_name}")
    subcategories = category.subcategory_set.all()

    positions = Position.objects.filter(subcategory__in=subcategories)
    categories = Category.objects.all()

    for position in positions:
        if str(position.id) in liked_positions:
            position.liked = True
        else:
            position.liked = False

    return render(
        request,
        "positions/category_detail.html",
        {
            "categories": categories,
            "category": category,
            "subcategories": subcategories,
            "positions": positions,
            "liked_positions": liked_positions,
        },
    )
