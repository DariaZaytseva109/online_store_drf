from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser

from online_store_app.models import Product, Category, Basket, BasketProduct, Image
from online_store_app.permissions import IsOwner, IsOwnerBasketProduct
from online_store_app.serializers import ProductSerializer, CategorySerializer, BasketSerializer, \
    BasketProductSerializer2, BasketProductCreateSerializer, BasketCleanSerializer, ImageSerializer, \
    BasketCreateSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    http_method_names = ['get']
    serializer_class = ProductSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    http_method_names = ['get']
    serializer_class = CategorySerializer


class BasketView(generics.RetrieveAPIView):
    queryset = Basket.objects.all()
    http_method_names = ['get']
    serializer_class = BasketSerializer
    permission_classes = (IsOwner, )


class AllBasketView(generics.ListAPIView):
    queryset = Basket.objects.all()
    http_method_names = ['get']
    serializer_class = BasketSerializer
    permission_classes = (IsAdminUser, )


class BasketProductViewCreate(generics.CreateAPIView):
    queryset = BasketProduct.objects.all()
    serializer_class = BasketProductCreateSerializer
    permission_classes = (IsOwnerBasketProduct,)


class BasketProductViewUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = BasketProduct.objects.all()
    serializer_class = BasketProductSerializer2
    permission_classes = (IsOwnerBasketProduct,)

class BasketViewClean(generics.RetrieveUpdateAPIView):
    queryset = Basket.objects.all()
    http_method_names = ['get', 'post', 'put']
    serializer_class = BasketCleanSerializer
    permission_classes = (IsOwner,)


class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    http_method_names = ['get']
    serializer_class = ImageSerializer


class BasketCreateView(generics.CreateAPIView):
    queryset = BasketProduct.objects.all()
    serializer_class = BasketCreateSerializer







