from rest_framework.routers import DefaultRouter
from django.urls import path

from online_store_app.views import ProductView, \
    CategoryView, BasketView, AllBasketView, \
    BasketProductViewCreate, BasketProductViewUpdate, BasketViewClean \

urlpatterns = [
    path('basket/', AllBasketView.as_view()),
    path('basket/<int:pk>/', BasketView.as_view()),  # просмотр корзины
    path('basketproduct/add/', BasketProductViewCreate.as_view()),  # добавление продукта в корзину
    path('basketproduct/<int:pk>/', BasketProductViewUpdate.as_view()),  # изменение кол-ва
    path('basket/clean/<int:pk>/', BasketViewClean.as_view())
    ]
router = DefaultRouter()
router.register('products', ProductView)
router.register('categories', CategoryView)



urlpatterns.extend(router.urls)
