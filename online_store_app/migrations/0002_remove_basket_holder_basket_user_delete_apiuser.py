# Generated by Django 4.2.7 on 2023-11-03 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('online_store_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='holder',
        ),
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ApiUser',
        ),
    ]
