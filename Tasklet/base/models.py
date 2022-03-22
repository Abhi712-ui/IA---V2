
from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Category(models.Model):
     Category_User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
     Header = models.CharField(max_length=250, null=True, blank=True)

     def __str__(self):
         return f"{self.Header}"
     

class Task(models.Model):
     Task_Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
     title = models.CharField(max_length=250)
     description = models.TextField(null=True, blank=True)
     complete = models.BooleanField(default=False)
     created = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return f"{self.title}"

     class Meta:
          ordering = ['complete'] 

