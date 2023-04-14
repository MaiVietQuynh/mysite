# Generated by Django 4.0.4 on 2022-05-26 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='avatar',
            new_name='img',
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=True, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
