from django.db import models

# Create your models here.
class Promotion(models.Model):
    description=models.TextField()
    coupon=models.CharField(max_length=6)


class Collection(models.Model):
    title=models.CharField(max_length=255)
    feature_product=models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

class Product(models.Model):
    collection=models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions=models.ManyToManyField(Promotion)
    slug=models.SlugField(default='-')
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)


class Customer(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'
    MEMBERSHIP=[
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    birth_date=models.DateField(null=True)
    choice_field=models.CharField(max_length=1, choices=MEMBERSHIP, default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PENDING='P'
    COMPLETE='C'
    FAILED='F'
    PAYMENT_STATUS=[
        (PENDING, 'Pending'),
        (COMPLETE, 'Complete'),
        (FAILED, 'Failed')
    ]
    customer=models.ForeignKey(Customer, on_delete=models.PROTECT)
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1, choices=PAYMENT_STATUS, default=PENDING)


class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.PROTECT)
    product=models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    customer=models.OneToOneField(Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    created_at=models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    Product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()