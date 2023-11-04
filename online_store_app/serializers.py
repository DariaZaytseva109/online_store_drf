from rest_framework import serializers

from online_store_app.models import Product, Subcategory, Category, Basket


class ProductSerializer(serializers.ModelSerializer):
    subcategory = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'slug', 'price', 'subcategory']


class SubcategorySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True, read_only=True)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Subcategory
        fields = ['name', 'products', 'category']


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'subcategories']


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ['user', 'products']