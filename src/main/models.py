from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=50, blank=False)
  price = models.DecimalField(max_digits=6,decimal_places=2, blank=False)
  release_date = models.DateField(blank=True)
  first_date_available = models.DateField(auto_now_add=True)
  model = models.CharField(max_length=50, blank=False)
  asin = models.CharField(max_length=50, blank=False)
  image = models.ImageField(blank=True, null=True, upload_to='product')

  def __str__(self):
    return f"{self.name} ({self.price})"