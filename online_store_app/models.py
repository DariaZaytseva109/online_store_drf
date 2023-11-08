from django.conf import settings
from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Наименование'
    )
    slug = models.SlugField(max_length=15, unique=True)
    image_small = models.ForeignKey(
        "Image",
        null=True, blank=True,
        verbose_name='Фото мал.',
        on_delete=models.SET_NULL,
        related_name='image_small'
    )
    image_medium = models.ForeignKey(
        "Image",
        null=True, blank=True,
        verbose_name='Фото ср.',
        on_delete=models.SET_NULL,
        related_name='image_medium'
    )
    image_large = models.ForeignKey(
        "Image",
        null=True, blank=True,
        verbose_name='Фото бол.',
        on_delete=models.SET_NULL,
        related_name='image_large'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )
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
    image = models.ForeignKey(
        "Image",
        null=True, blank=True,
        verbose_name='Фото',
        on_delete=models.SET_NULL
    )
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
    image = models.ForeignKey(
        "Image",
        null=True, blank=True,
        verbose_name='Фото',
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"


class Basket(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class BasketProduct(models.Model):
    basket = models.ForeignKey(
        'Basket',
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='basketproduct',
        verbose_name='Корзина-Продукт')
    product = models.ForeignKey(
        'Product',
        null=True,
        on_delete=models.CASCADE,
        related_name='basketproduct',
        verbose_name='Продукт')
    quantity = models.PositiveIntegerField(
        verbose_name='Количество'
    )


class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"
