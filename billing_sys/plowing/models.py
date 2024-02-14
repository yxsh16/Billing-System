from django.db import models
from billing_sys.utils.models import BaseModel

# Create your models here.

class PlowingService(BaseModel):
    provider = models.ForeignKey('users.User', on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    

class PlowingRequest(BaseModel):
    service = models.ForeignKey('plowing.PlowingService', on_delete = models.CASCADE)
    requester = models.ForeignKey('users.User', on_delete = models.CASCADE)
    status = models.CharField(max_length=10, choices= [('pending', 'Pending'), 
                                                       ('accepted', 'Accepted'), ('rejected', 'Rejected'), 
                                                       ('completed', 'Completed')], default='pending')
    