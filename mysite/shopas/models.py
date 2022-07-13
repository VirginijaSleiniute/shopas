from django.db import models
from django.contrib.auth.models import User
from datetime import date
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Item(models.Model):
    title = models.CharField(max_length=200)
    designer = models.ForeignKey('Designer', on_delete=models.SET_NULL, null=True, related_name='items')
    summary = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    category = models.ManyToManyField(Category)
    photo = models.ImageField('Photo', upload_to='photos', null=True, blank=True)

    def display_category(self):
        return ', '.join(category.name for category in self.category.all())

    display_category.short_description = 'Category'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class Designer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = HTMLField("Description", null=True, blank=True)

    def display_items(self):
        return ', '.join(item.title for item in self.items.all())

    display_items.short_description = 'Items'


    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Designer'
        verbose_name_plural = 'Designers'


class Cart(models.Model):
    created_add = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='carts')

    def __str__(self):
        return f'{self.item} {self.quantity}'


    ORDER_STATUS = (
        ('a', 'Accepted'),
        ('i', 'In Progress'),
        ('d', 'Done'),
        ('c', 'Cancelled'),
        ('k', 'Cart'),
    )

    status = models.CharField(
        max_length=1,
        choices=ORDER_STATUS,
        blank=True,
        default='k',
        help_text='Status',
    )


    @property
    def get_total(self):
        orderitems = self.order_lines.all()
        total = sum([item.get_total for item in orderitems])
        return total 


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderLine(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, verbose_name="Cart", on_delete=models.SET_NULL, null=True, related_name='order_lines')
    qty = models.IntegerField(verbose_name="Quantity")

    @property
    def get_total(self):
        total = self.item.price * self.qty
        return total

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'




    