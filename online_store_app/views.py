from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from online_store_app.models import Product, Category, Subcategory, Basket
#from online_store_app.permissions import IsOwner
from online_store_app.serializers import ProductSerializer, CategorySerializer, SubcategorySerializer, BasketSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    http_method_names = ['get']
    serializer_class = ProductSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    http_method_names = ['get']
    serializer_class = CategorySerializer


#class SubcategoryView(viewsets.ModelViewSet):
    #queryset = Subcategory.objects.all()
    #http_method_names = ['get']
    #serializer_class = SubcategorySerializer


class BasketView(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    http_method_names = ['get', 'post', 'put']
    serializer_class = BasketSerializer


        #user_id = request.user


    #permission_classes = [IsOwner]



