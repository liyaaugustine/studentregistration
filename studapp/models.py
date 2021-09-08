from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    status=models.CharField(max_length=20,default='active')
class Registraion(models.Model):
    name=models.CharField(max_length=30)
    contact=models.BigIntegerField()
    email=models.CharField(max_length=30)
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,default='active')
class AdminLogin(models.Model):
    adminuname=models.CharField(max_length=20)
    adminpassword=models.CharField(max_length=10)
