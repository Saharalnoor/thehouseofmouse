# Generated by Django 2.2.6 on 2019-10-22 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image1',
            field=models.ImageField(upload_to='product_images'),
        ),
    ]
