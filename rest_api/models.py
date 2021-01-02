from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Plant(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics')
    price=models.IntegerField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,)
    plant=models.ForeignKey(Plant,on_delete=models.CASCADE,)
    quantity=models.IntegerField()
    address=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)