from rest_framework import serializers

from online_store_app.models import Product, Subcategory, Category, Basket, BasketProduct


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


class BasketProductSerializer(serializers.ModelSerializer):
    product = ProductInBasketSerializer()
    subtotal = serializers.SerializerMethodField()

    def get_subtotal(self, obj):
        return obj.product.price * obj.quantity

    class Meta:
        model = BasketProduct
        fields = ['product', 'quantity', 'subtotal']


class BasketSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    basketproduct = BasketProductSerializer(many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, obj):
        total = 0
        for bp in obj.basketproduct.all():
            total += bp.product.price * bp.quantity
        return {"total": total}

    class Meta:
        model = Basket
        fields = ['user', 'basketproduct', 'total']