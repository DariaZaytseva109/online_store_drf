from rest_framework.routers import DefaultRouter
from django.urls import path

from online_store_app.views import ProductView, \
    CategoryView, BasketView, \
    BasketProductViewCreate, BasketProductViewUpdate, \
    BasketViewClean, ImageView, BasketCreateView

urlpatterns = [
    path('basket/', BasketCreateView.as_view()),                         # создание корзины
    path('basket/<int:pk>/', BasketView.as_view()),                      # просмотр корзины
    path('basketproduct/add/', BasketProductViewCreate.as_view()),       # добавление продукта в корзину
    path('basketproduct/<int:pk>/', BasketProductViewUpdate.as_view()),  # изменение кол-ва
    path('basket/clean/<int:pk>/', BasketViewClean.as_view()),           # очищение корзины
    path('images/<str:image_file>/', ImageView.as_view({'get': 'list'}))
    ]
router = DefaultRouter()
router.register('products', ProductView)
router.register('categories', CategoryView)


urlpatterns.extend(router.urls)
