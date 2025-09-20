from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Wearables', 'Wearables'),
        ('SmartPhone', 'SmartPhone'),
        ('Laptop', 'Laptop'),
        ('Camera', 'Camera'),
        ('Audio', 'Audio'),
        ('Mouse', 'Mouse'),
        ('Keyboard', 'Keyboard'),
        ('Monitor', 'Monitor'),
        ('Processor', 'Processor'),
        ('Graphics Card', 'Graphics Card'),
    ]

    product_image = models.ImageField(upload_to='products/', blank=True, null=True)
    product_category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Wearables'
        )

    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} ({self.product_category})"