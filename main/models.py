from django.db import models

class masterSignup(models.Model):
    id = models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    contact=models.IntegerField(null=True)
    email=models.EmailField(max_length=100)
    address=models.CharField(max_length=250)
    profile=models.FileField(upload_to='media/',null=True)
    username = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.email