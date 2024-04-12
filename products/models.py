from django.db import models
from django.utils.translation import gettext_lazy as _
from media.utils import validate_phone_number


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    created_at = models.DateTimeField(_("Created_at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class Product(models.Model):
    class SizeType(models.TextChoices):
        S = 'S'
        M = 'M'
        L = 'L'
        XL = 'XL'

    title = models.CharField(_("Title"), max_length=100)
    price = models.IntegerField(_("Price"))
    short_desc = models.TextField(_("Short Description"))
    size = models.CharField(_("Size"), max_length=20, choices=SizeType.choices)
    quantity = models.IntegerField(_("quantity"), default=0)
    product_image_view = models.ForeignKey("media.Media",
                                           on_delete=models.CASCADE,
                                           verbose_name=_("Product Image View"),
                                           related_name="product_image_view")
    product_description = models.TextField(_("Product Description"))
    reviews = models.CharField(_("Reviews"), max_length=20)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name=_("Category"))
    tags = models.ForeignKey("Tag",
                             on_delete=models.CASCADE,
                             verbose_name=_("Tags"))

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ForeignKey("media.Media", on_delete=models.CASCADE,
                              verbose_name=_("image"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"),
                                related_name="product_images")

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

    def __str__(self):
        return f"Image Id: {self.id} | Product: {self.product.title}"


class Tag(models.Model):
    title = models.CharField(_("Tags"), max_length=100)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.title


class ProductCart(models.Model):
    title = models.CharField(_("title"), max_length=100)
    price = models.CharField(_("price"), max_length=50)
    quantity = models.IntegerField(_("quantity"), default=0)
    product_cart_image = models.ForeignKey("media.Media",
                                           on_delete=models.CASCADE,
                                           verbose_name=_("Product Cart Image"),
                                           related_name="product_cart_image")
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name=_("product"),
                                related_name="product_cart")
    total_price = models.FloatField(_("Total"), default=0)

    class Meta:
        verbose_name = _("Product Cart")
        verbose_name_plural = _("Product Carts")

    def __str__(self):
        return self.title


class ProductCheckout(models.Model):
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    country = models.CharField(_("Country/Region"), max_length=100)
    city = models.CharField(_("Town/City"), max_length=100)
    street_address = models.CharField(_("Street Address"), max_length=100)
    state = models.CharField(_("State"), max_length=100)
    phone_number = models.CharField(_("Phone Number"), max_length=20,
                                    validators=[validate_phone_number])
    order_notes = models.TextField(_("Order Notes"))

    class Meta:
        verbose_name = _("Product Checkout")
        verbose_name_plural = _("Product Checkouts")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ProductCheckoutOrder(models.Model):
    order = models.ForeignKey(ProductCheckout, on_delete=models.CASCADE, verbose_name=_("order"))
    quantity = models.CharField(_("quantity"), default=0, max_length=50)
    subtotal = models.CharField(_("Subtotal"), max_length=50)
    coupon_discount = models.CharField(_("Coupon Discount"), max_length=200)
    shipping = models.CharField(_("Shipping"), max_length=50)
    total_price = models.CharField(_("Total"), max_length=50)
    product_checkout_order_image = models.ForeignKey("media.Media",
                                                     on_delete=models.CASCADE,
                                                     verbose_name=_("Product Checkout Order Image"),
                                                     related_name="product_checkout_order_image")
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name=_("product"),
                                related_name="product_checkout_order")

    class Meta:
        verbose_name = _("Product Checkout Order")
        verbose_name_plural = _("Product Checkout Orders")
        unique_together = ['order', 'product']

    def __str__(self):
        return self.title


class OrderConfirmationDetails(models.Model):
    title = models.CharField(_("title"), max_length=100)
    quantity = models.CharField(_("Quantity"), max_length=30)
    subtotal = models.CharField(_("Subtotal"), max_length=30)
    shipping = models.CharField(_("Shipping"), max_length=30)
    total_price = models.CharField(_("Total"), max_length=30)
    order_confirmation_details_image = models.ForeignKey("media.Media",
                                                         on_delete=models.CASCADE,
                                                         verbose_name=_("Order Confirmation Details Image"),
                                                         related_name="order_confirmation_details_image")

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name=_("product"),
                                related_name="product_confirmation_order_details")

    class Meta:
        verbose_name = _("Order Confirmation Detail")
        verbose_name_plural = _("Order Confirmation Details")

    def __str__(self):
        return self.title

    @property
    def subtotal(self):
        return self.product.price * self.quantity

    @property
    def total_price(self):
        return f"{(self.product.price * self.quantity) + self.shipping}"
