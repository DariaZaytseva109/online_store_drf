from rest_framework import viewsets

from online_store_app.models import Product, Category, Subcategory
from online_store_app.serializers import ProductSerializer, CategorySerializer, SubcategorySerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    http_method_names = ['get']
    serializer_class = ProductSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    http_method_names = ['get']
    serializer_class = CategorySerializer


class SubcategoryView(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    http_method_names = ['get']
    serializer_class = SubcategorySerializer



