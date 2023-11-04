from django.conf import settings
from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Наименование'
    )
    slug = models.SlugField(max_length=15, unique=True)
    # image = None
    price = models.PositiveIntegerField(verbose_name='Цена')
    subcategory = models.ForeignKey(
        'Subcategory',
        null=True,
        on_delete=models.SET_NULL,
        related_name='products',
        verbose_name='Подкатегория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"


class Subcategory(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Наименование')
    slug = models.SlugField(max_length=15, unique=True)
    # image = None
    category = models.ForeignKey(
        'Category',
        null=True,
        on_delete=models.SET_NULL,
        related_name='subcategories',
        verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегории"
        verbose_name_plural = "Подкатегории"


class Category(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Наименование'
    )
    slug = models.SlugField(max_length=15, unique=True)
    # image = None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"


class Basket(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    products = models.ManyToManyField(
        'Product',
        blank=True,
        related_name='products'
    )

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"



