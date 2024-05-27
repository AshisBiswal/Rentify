from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f'{self.user.username}'
    


class Property(models.Model):
    RENT = 'RENT'
    SELL = 'SELL'
    TYPE_CHOICES = [
        (RENT, 'Rent'),
        (SELL, 'Sell'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name =  models.CharField(max_length=250,default='No_Name')
    place = models.CharField(max_length=250)
    area = models.CharField(max_length=250)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    nearby_landmark = models.CharField(max_length=250, blank=True, null=True)
    property_type = models.CharField(max_length=4, choices=TYPE_CHOICES, default=RENT)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=500)  # New price field
    #image = models.ImageField(upload_to='property_images/', blank=True, null=True)  # Image field
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.place} - {self.user.username}"
    
class Like(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    property =  models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} likes {self.property.place}"
    

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.property.place}"