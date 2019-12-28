from django.db import models

# Create your models here.
class Product(models.Model):
    PName = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    Price = models.DecimalField(max_digits=100, decimal_places=3)
    Weight = models.IntegerField(blank=True,default=0)
    Thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.PName
    