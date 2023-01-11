from django.db import models

class Vehicle(models.Model):

    owner = models.CharField(max_length=255)
    license_number = models.CharField(max_length=20)
    mobile_number = models.CharField( max_length=20)
    model = models.CharField(max_length=256)
    role = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
    def __str__(self):  
        return self.owner
