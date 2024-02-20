from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50,default="NaN")
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    ppic = models.ImageField(default='images/default.jpg', upload_to='images/')
    fav = models.BooleanField(default=False)
    def __str__(self):
        return self.name

