# Generated by Django 4.2.7 on 2023-11-06 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_store_app', '0005_remove_basket_products_basket_total_basketproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='total',
        ),
        migrations.RemoveField(
            model_name='basketproduct',
            name='subtotal',
        ),
    ]