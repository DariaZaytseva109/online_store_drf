# Generated by Django 4.2.7 on 2023-11-06 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store_app', '0007_alter_subcategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cat_image', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_large',
            field=models.ImageField(blank=True, null=True, upload_to='prod_image_large', verbose_name='Фото бол.'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_medium',
            field=models.ImageField(blank=True, null=True, upload_to='prod_image_med', verbose_name='Фото ср.'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_small',
            field=models.ImageField(blank=True, null=True, upload_to='prod_image_small', verbose_name='Фото мал.'),
        ),
    ]
