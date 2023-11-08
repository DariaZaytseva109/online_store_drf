from rest_framework import serializers

from online_store_app.models import Product, Subcategory, Category, Basket, BasketProduct, Image


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
    price = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = ['id',
            'name',
            'price',
        ]


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
    product = ProductInBasketSerializer(read_only=True)
    subtotal = serializers.SerializerMethodField(read_only=True)

    def get_subtotal(self, obj):
        return obj.product.price * obj.quantity

    class Meta:
        model = BasketProduct
        fields = ['product', 'quantity', 'subtotal']


class BasketSerializer(serializers.ModelSerializer):
    basketproduct = BasketProductSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    def get_total(self, obj):
        total = 0
        for bp in obj.basketproduct.all():
            total += bp.product.price * bp.quantity
        return {"total": total}
    class Meta:
        model = Basket
        fields = ['user', 'basketproduct', 'total']


class BasketSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ['pk']

class ProductInBasketSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pk']


class BasketProductSerializer2(serializers.ModelSerializer):

    product = ProductInBasketSerializer2(read_only=True)
    quantity = serializers.IntegerField()
    class Meta:
        model = BasketProduct
        fields = ['product', 'quantity']


class BasketProductCreateSerializer(serializers.ModelSerializer):
    basket = BasketSerializer2(read_only=True)
    product = ProductInBasketSerializer2
    quantity = serializers.IntegerField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = BasketProduct
        fields = ['basket', 'product', 'quantity', 'user']

    def create(self, validated_data):
        print(validated_data)
        user = validated_data['user']
        basket = Basket.objects.get(user=user)
        product = validated_data['product']
        quantity = validated_data['quantity']
        return BasketProduct(basket=basket, product=product, quantity=quantity)


class BasketCleanSerializer(serializers.ModelSerializer):

    def update(self, obj, validated_data):
        for bp in obj.basketproduct.all():
            bp.delete()
        return obj

    class Meta:
        model = Basket
        fields = ['user', 'basketproduct']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class BasketCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = BasketProduct
        fields = ['user']

    def create(self, validated_data):
        user = validated_data['user']
        new_basket = Basket.objects.create(user=user)
        return new_basket
