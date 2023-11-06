from rest_framework.routers import DefaultRouter

from online_store_app.views import ProductView, CategoryView, BasketView, BasketProductView

router = DefaultRouter()
router.register('products', ProductView)
router.register('categories', CategoryView)
#router.register('subcategories', SubcategoryView)
router.register('basket', BasketView)
#router.register('basketproduct', BasketProductView)





urlpatterns = []

urlpatterns.extend(router.urls)
