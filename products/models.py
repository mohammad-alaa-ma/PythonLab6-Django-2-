from django.db import models
import uuid

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Product Name")
    code = models.CharField(max_length=50, unique=True, verbose_name="Product Code")
    description = models.TextField(verbose_name="Product Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Product Image")
    in_stock = models.PositiveIntegerField(default=0, verbose_name="Items in Stock")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.code}"
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)
