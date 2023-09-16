from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY = (
        ('Building Materials' , 'Building Materials'),
        ('Tools and Equipmen' , 'Tools and Equipmen'),
        ('Heavy Machinery Parts' , 'Heavy Machinery Parts'),
)

class Product(models.Model) :
        name = models.CharField(max_length=200 , null=True)
        category = models.CharField(max_length=100 , choices=CATEGORY , null=True)
        quantity = models.PositiveIntegerField(null=True)

        class Meta :
            verbose_name_plural = "product"

        def __str__(self):
                return f'{self.name}'
        

class Order(models.Model):
        product = models.ForeignKey(Product , on_delete=models.CASCADE , null=True)
        staff = models.ForeignKey(User , models.CASCADE , null=True)
        order_quantity = models.PositiveIntegerField(null = True)
        date = models.DateTimeField(auto_now_add=True)

        class Meta :
            verbose_name_plural = "Order"

        def __str__(self):
            staff_username = self.staff.username if self.staff else "Unknown"
            return f'{self.product} - commander par : {staff_username}'