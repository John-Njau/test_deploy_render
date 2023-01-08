from django.db import models

# Create your models here.
class Watch(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name