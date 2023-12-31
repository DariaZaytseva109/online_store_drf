# Generated by Django 4.2.7 on 2023-11-04 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store_app', '0003_alter_basket_options_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_large',
            field=models.ImageField(null=True, upload_to='prod_image_large', verbose_name='Фото бол.'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_medium',
            field=models.ImageField(null=True, upload_to='prod_image_med', verbose_name='Фото ср.'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_small',
            field=models.ImageField(null=True, upload_to='prod_image_small', verbose_name='Фото мал.'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(null=True, upload_to='subcat_image', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='cat_image', verbose_name='Фото'),
        ),
    ]
