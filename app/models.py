from django.db import models

# Create your models here.

class Mobile(models.Model):

    
    STATUS = [
        ('0','کارکرده'),
        ('1','آکبند'),
    ]
    ram = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    cpu = models.CharField(max_length=64,null=True)
    
    title = models.CharField(max_length=63, null=True )
    description = models.TextField(max_length=512,null=True)
    manufacturer = models.ForeignKey('manufacturer', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=1, choices=STATUS, null=True)
    


class Manufacturer(models.Model):
    title = models.CharField(max_length=127, null=True)
    description = models.TextField(max_length=2000, null=True)


    def __str__(self):
        return self.title