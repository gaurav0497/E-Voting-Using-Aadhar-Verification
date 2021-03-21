from django.db import models
from datetime import datetime

# Create your models here.
class Candidate(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    party_name = models.CharField(max_length=50, default="")
    district = models.CharField(max_length=50, default="")
    gender = models.CharField(max_length=50,default="")
    mobile = models.IntegerField()
    aadhar_number = models.IntegerField()
    register_date = models.DateField(default=datetime.now())

    def __str__(self):
        return self.name