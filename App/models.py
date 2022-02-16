from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Product(models.Model):
    CATEGORY = (
        (0, _('cheap')),
        (1, _('intermediate')),
        (2, _('premium'))
    )

    product = models.CharField(max_length= 100)
    product_name = models.CharField(max_length= 200)
    price = models.FloatField()
    category = models.IntegerField(choices= CATEGORY, default= 1)
    image = models.ImageField(upload_to= 'images', max_length=254)