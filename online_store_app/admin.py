from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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
    list_display = ['user']
    list_display_links = ['user']
    list_per_page = 10
    search_fields = ['user']


class BasketProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']
    list_display_links = ['product']
    list_per_page = 10
    search_fields = ['product']


admin.site.register(Product, ProductAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(BasketProduct, BasketProductAdmin)
