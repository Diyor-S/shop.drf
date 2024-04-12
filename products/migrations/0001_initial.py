# Generated by Django 5.0.2 on 2024-04-12 11:25

import django.db.models.deletion
import media.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media', '0002_commonsettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductCheckout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('country', models.CharField(max_length=100, verbose_name='Country/Region')),
                ('city', models.CharField(max_length=100, verbose_name='Town/City')),
                ('street_address', models.CharField(max_length=100, verbose_name='Street Address')),
                ('state', models.CharField(max_length=100, verbose_name='State')),
                ('phone_number', models.CharField(max_length=20, validators=[media.utils.validate_phone_number], verbose_name='Phone Number')),
                ('order_notes', models.TextField(verbose_name='Order Notes')),
            ],
            options={
                'verbose_name': 'Product Checkout',
                'verbose_name_plural': 'Product Checkouts',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('short_desc', models.TextField(verbose_name='Short Description')),
                ('size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'Xl')], max_length=20, verbose_name='Size')),
                ('quantity', models.IntegerField(default=0, verbose_name='quantity')),
                ('product_description', models.TextField(verbose_name='Product Description')),
                ('reviews', models.CharField(max_length=20, verbose_name='Reviews')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Category')),
                ('product_image_view', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image_view', to='media.media', verbose_name='Product Image View')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Product View',
                'verbose_name_plural': 'Product Views',
            },
        ),
        migrations.CreateModel(
            name='OrderConfirmationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('quantity', models.CharField(max_length=30, verbose_name='Quantity')),
                ('shipping', models.CharField(max_length=30, verbose_name='Shipping')),
                ('order_confirmation_details_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_confirmation_details_image', to='media.media', verbose_name='Order Confirmation Details Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_confirmation_order_details', to='products.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'order confirmation detail',
                'verbose_name_plural': 'order confirmation details',
            },
        ),
        migrations.CreateModel(
            name='ProductCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('price', models.CharField(max_length=50, verbose_name='price')),
                ('quantity', models.IntegerField(default=0, verbose_name='quantity')),
                ('total_price', models.FloatField(default=0, verbose_name='Total')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_cart', to='products.product', verbose_name='product')),
                ('product_cart_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_cart_image', to='media.media', verbose_name='Product Cart Image')),
            ],
            options={
                'verbose_name': 'product cart',
                'verbose_name_plural': 'product carts',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.media', verbose_name='image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='products.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'product image',
                'verbose_name_plural': 'product images',
            },
        ),
        migrations.CreateModel(
            name='ProductCheckoutOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(default=0, max_length=50, verbose_name='quantity')),
                ('subtotal', models.CharField(max_length=50, verbose_name='Subtotal')),
                ('coupon_discount', models.CharField(max_length=200, verbose_name='Coupon Discount')),
                ('shipping', models.CharField(max_length=50, verbose_name='Shipping')),
                ('total_price', models.CharField(max_length=50, verbose_name='Total')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcheckout', verbose_name='order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_checkout_order', to='products.product', verbose_name='product')),
                ('product_checkout_order_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_checkout_order_image', to='media.media', verbose_name='Product Checkout Order Image')),
            ],
            options={
                'verbose_name': 'product checkout order',
                'verbose_name_plural': 'product checkout orders',
                'unique_together': {('order', 'product')},
            },
        ),
    ]
