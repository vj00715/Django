from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class teacherSignup(models.Model):
    id = models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=225)
    lastname=models.CharField(max_length=225)
    contact=models.IntegerField(null=True)
    email=models.EmailField(max_length=225)
    address=models.CharField(max_length=225)
    profile=models.FileField(upload_to='media/',null=True)
    username = models.CharField(max_length=225,null=True)
    salary = models.FloatField(default=0)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.email

        