from rest_framework.routers import DefaultRouter

from online_store_app.views import ProductView, CategoryView, SubcategoryView

router = DefaultRouter()
router.register('products', ProductView)
router.register('categories', CategoryView)
router.register('subcategories', SubcategoryView)

urlpatterns = []

urlpatterns.extend(router.urls)
