# Generated by Django 4.0.4 on 2022-05-26 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_avatar_product_img_product_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
