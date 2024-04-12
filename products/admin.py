from django.contrib import admin
from products.models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'size', 'quantity',
                    'reviews', 'category', 'tags']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image']


@admin.register(ProductCart)
class ProductCartAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'quantity', 'product',
                    'total_price']


class ProductCheckoutOrderInLine(admin.TabularInline):
    model = ProductCheckoutOrder
    extra = 2


@admin.register(ProductCheckout)
class ProductCheckoutAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'country', 'city',
                    'street_address', 'state', 'phone_number']
    inlines = [ProductCheckoutOrderInLine]




@admin.register(OrderConfirmationDetails)
class OrderConfirmationDetailsAdmin(admin.ModelAdmin):
    list_display = ['title', 'quantity', 'subtotal',
                    'shipping', 'total_price', 'product']
