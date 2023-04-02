from django.db import models

# Create your models here.
class Vehicles(models.Model):
    PETROL = 0
    DIESEL = 1
    CNG = 2

    FUEL_CHOICE = (
        (PETROL, 'Petrol'),
        (DIESEL, 'Deisel'),
        (CNG, 'Cng'),
    )
    brand = models.CharField(blank=True, null=True, max_length=512)
    price = models.CharField(blank=True, null=True, max_length=100)
    fuel = models.PositiveSmallIntegerField(choices=FUEL_CHOICE, blank=True, null=True)
    seat = models.IntegerField(blank=True, null=True)
    enginenumber = models.CharField(blank=True, null=True, max_length=100)
    colour = models.CharField(blank=True, null=True, max_length=100)
    model = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True )
    img_url = models.URLField(max_length=512, blank=True, null=True)
    detail_link = models.URLField(max_length=512)

    def __str__(self):
        return '{0}-{1}-{2}-{3}'.format(self.brand, self.price, self.fuel, self.model)