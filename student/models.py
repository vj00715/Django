from django.db import models

class studentSignup(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    profile = models.FileField(upload_to='media/',null=True)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.email