from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.


class users(models.Model):
    admin = models.ForeignKey(User, on_delete = models.CASCADE)
    contact_number = models.CharField(max_length=13)
    Address=models.TextField()
    gender = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_pic=models.FileField(upload_to='workers_pic/')

class workers(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=13)
    dob = models.DateField(null=True, blank=True)
    Address = models.TextField()
    city=models.CharField(max_length=255)
    gender = models.CharField(max_length=250)
    designation=models.CharField(max_length=255)
    profile_pic=models.FileField(upload_to='workers_pic/')
    acc_activation=models.BooleanField(default=False)
    avalability_status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Country(models.Model):
    name = models.CharField(max_length=150)


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)


class City(models.Model):
    state = models.CharField(max_length=150)
    name = models.CharField(max_length=150)

class ServiceCatogarys(models.Model):
    img=models.ImageField(upload_to='catogry_imgs')
    Name=models.CharField(max_length=255)
    Description=models.TextField()
    
class ServiceRequests(models.Model):
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    Problem_Description=models.TextField()
    service = models.ForeignKey(ServiceCatogarys, on_delete=models.CASCADE)
    Address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    pin = models.CharField(max_length=10)
    House_No = models.CharField(max_length=20)
    landmark = models.TextField(null=True)
    contact=models.CharField(max_length=200)
    status=models.BooleanField(default=False)
    dateofrequest=models.DateTimeField(auto_now_add=True)

class Response(models.Model):
    requests=models.ForeignKey(ServiceRequests,on_delete=models.CASCADE)
    assigned_worker=models.ForeignKey(workers,on_delete=models.CASCADE)
    Date=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)


class Feedback(models.Model):
    Rating=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    Description=models.TextField()
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    # User=models.ForeignKey(users,on_delete=models.CASCADE)
    Employ=models.ForeignKey(workers,on_delete=models.CASCADE)
    Date=models.DateField()


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    forget_token = models.CharField(max_length=1000)



