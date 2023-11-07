from django.contrib import admin

from .models import Product, Subcategory, Category, Basket, BasketProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'subcategory']
    list_display_links = ['name']
    list_per_page = 10
    search_fields = ['name']


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_display_links = ['name']
    list_per_page = 10
    search_fields = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    list_per_page = 10
    search_fields = ['name']


class BasketAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    list_display_links = ['id', 'user']
    list_per_page = 10
    search_fields = ['id', 'user']


class BasketProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'basket', 'product', 'quantity']
    list_display_links = ['id', 'basket', 'product']
    list_per_page = 10
    search_fields = ['basket', 'product']


admin.site.register(Product, ProductAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(BasketProduct, BasketProductAdmin)
