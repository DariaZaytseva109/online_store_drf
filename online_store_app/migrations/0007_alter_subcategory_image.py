# Generated by Django 4.2.7 on 2023-11-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store_app', '0006_remove_basket_total_remove_basketproduct_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='subcat_image', verbose_name='Фото'),
        ),
    ]