from django.urls import path

from restaurant.positions.api.views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryUpdateView,
    GetByIdsView,
    PositionCreateView,
    PositionDeleteView,
    PositionUpdateView,
    SearchAPIView,
    SubCategoryCreateView,
    SubCategoryDeleteView,
    SubCategoryUpdateView,
    TipDetailView,
    TipListCreateView,
)
from restaurant.positions.views import category_detail, index, tips_list

app_name = "positions"
urlpatterns = [
    path("", view=index, name="index"),
    path("tips/", view=tips_list, name="tips"),
    path("api/search/", SearchAPIView.as_view(), name="api-search"),
    path("api/ids/", GetByIdsView.as_view(), name="api-get-by-ids"),
    path("api/position/", PositionCreateView.as_view(), name="position-create"),
    path("api/position/<int:pk>/", PositionUpdateView.as_view(), name="position-update"),
    path(
        "api/position/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete",
    ),
    path("<str:category_name>/", category_detail, name="category_detail"),
    path("api/subcategories/", SubCategoryCreateView.as_view(), name="subcategory-create"),
    path(
        "api/subcategories/<int:pk>/delete/",
        SubCategoryDeleteView.as_view(),
        name="subcategory-delete",
    ),
    path(
        "api/subcategories/<int:pk>/",
        SubCategoryUpdateView.as_view(),
        name="subcategory-update",
    ),
    path("api/tips/", TipListCreateView.as_view(), name="tip-list-create"),
    path("api/tips/<int:pk>/", TipDetailView.as_view(), name="tip-detail"),
    # Category URLs
    path("api/categories/", CategoryCreateView.as_view(), name="category-create"),
    path(
        "api/categories/<int:pk>/delete/",
        CategoryDeleteView.as_view(),
        name="category-delete",
    ),
    path("api/categories/<int:pk>/", CategoryUpdateView.as_view(), name="category-update"),
]
