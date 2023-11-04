from rest_framework import serializers

from online_store_app.models import Product, Subcategory, Category, Basket


class ProductSerializer(serializers.ModelSerializer):
    subcategory = serializers.StringRelatedField(
        read_only=True)

    class Meta:
        model = Product
        fields = [
            'name', 'slug',
            'price', 'subcategory',
            'image_small', 'image_medium',
            'image_large']

class ProductInBasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'image_small']

class SubcategorySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(
        many=True, read_only=True)
    category = serializers.StringRelatedField(
        read_only=True)

    class Meta:
        model = Subcategory
        fields = ['name', 'products', 'category', 'image']


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.StringRelatedField(
        many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'subcategories', 'image']


class BasketSerializer(serializers.ModelSerializer):
    products = ProductInBasketSerializer(many=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Basket
        fields = ['user', 'products']
