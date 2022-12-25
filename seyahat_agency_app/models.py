from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from datetime import datetime

# 


class CategoryModel(models.Model):
    # id = models.Field(primary_key = True)
    title = models.TextField(null=True)
    keywords =  models.TextField(null=True)
    description =  models.TextField(null=True)
    #image
    #status
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return self.title

class PackageModel(models.Model):
    title = models.TextField(null=True)
    keywords =  models.TextField(null=True)
    description =  models.TextField(null=True)
    destination = models.CharField(max_length=200,null=True)
    status = models.BooleanField(False)
    detail = models.TextField(null=True)
    category_id = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    price = models.IntegerField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(null=True, max_length=30)
    image = models.CharField(max_length=50)
    package_id = models.ForeignKey(PackageModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
class Reservation(models.Model):
    
    username_id = models.ForeignKey(User,on_delete=models.CASCADE)
    package_id = models.ForeignKey(PackageModel,on_delete=models.CASCADE)
    startdate = models.DateField( auto_now_add=False)
    amount = models.IntegerField(default=1)
    note = models.CharField(null=False,max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

     
    def __str__(self):
        return self.package_id.title


class FAQ(models.Model):
     question = models.CharField(null=False, max_length=50)
     answer = models.CharField(null=False, max_length=50)
     created_at = models.DateField(auto_now_add=True)
     updated_at = models.DateField(auto_now_add=True)

     def __str__(self) -> str:
         return str(self.question[:5])+ "..."


class Comment(models.Model):

    title = models.CharField(null=False, max_length=50)
    rate = models.IntegerField(default =1 ,validators=[MinValueValidator(0), MaxValueValidator(100)])
    username_id = models.ForeignKey(User,on_delete=models.CASCADE)
    package_id = models.ForeignKey(PackageModel,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)


class SocialMedia(models.Model):
    name = models.CharField(null=False, max_length=10)

    def __str__(self) -> str:
        return self.name


class Setting(models.Model):
    title = models.CharField(null=False, max_length=50)
    keywords =  models.TextField(null=True)
    description =  models.TextField(null=True)
    company = models.TextField(null=False, max_length=20)
    address = models.TextField(null=False, max_length=20)
    phone = models.IntegerField()
    email = models.TextField(null=False, max_length=20)
    social = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)
    about_us = models.TextField(null=False, max_length=500)

