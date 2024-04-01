from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from restaurant.positions.api.serializers import (
    CategorySerializer,
    PositionSerializer,
    SubCategorySerializer,
    TipSerializer,
)
from restaurant.positions.models import Category, Position, SubCategory, Tip


class TipListCreateView(generics.ListCreateAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer


class TipDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


class SubCategoryCreateView(generics.CreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class SubCategoryDeleteView(generics.DestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAdminUser]


class SubCategoryUpdateView(generics.UpdateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


class PositionCreateView(generics.CreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class PositionDeleteView(generics.DestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAdminUser]


class PositionUpdateView(generics.UpdateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


class SearchAPIView(generics.ListAPIView):
    serializer_class = PositionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        query = self.request.query_params.get("q", "")
        positions = Position.objects.filter(name__icontains=query)

        return positions


class GetByIdsView(generics.ListAPIView):
    serializer_class = PositionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        ids_raw = self.request.query_params.get("ids", "")
        ids = ids_raw.split(",")
        positions = Position.objects.filter(id__in=ids)

        return positions
