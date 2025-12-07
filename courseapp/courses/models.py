from django.contrib.auth.models import AbstractUser
from django.db import models

from yaml import full_load_all


# Create your models here.
class User(AbstractUser):
    pass

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=False)
    def __str__(self):
        return self.name

class Course(BaseModel):
    subject = models.CharField(max_length=50,null=False)
    description = models.TextField()

    active = models.BooleanField(default=True)
    image= models.ImageField(upload_to='courses/%Y/%m',null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)