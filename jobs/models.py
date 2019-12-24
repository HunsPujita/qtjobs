from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class UserType(models.Model):
    UserType = models.CharField(primary_key=True, max_length=80)
    Description = models.CharField(max_length=100)


class Gender(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)


class Register(models.Model):
    UserID = models.CharField(primary_key=True, max_length=80)
    UserType = models.ForeignKey(UserType, max_length=80, on_delete=models.CASCADE)
    Email = models.EmailField(unique=True)
    MobileNumber = models.CharField(max_length=10, unique=True)
    GenderId = models.ForeignKey(Gender, on_delete=models.CASCADE)
    Location = models.CharField(max_length=200)


class Login(models.Model):
    UserID = models.ForeignKey(Register, primary_key=True, on_delete=models.CASCADE)
    Password = models.CharField(max_length=100)


class Resume(models.Model):
    UserID = models.ForeignKey(Register, primary_key=True, on_delete=models.CASCADE)
    Content = models.CharField(max_length=200)
    File = models.CharField(max_length=20)



