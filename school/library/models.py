from django.db import models
import datetime
from django.contrib.auth.models import User


class data(models.Model):
    book_name=models.CharField(max_length=50)
    author_name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)

class Record(models.Model):
    ename=models.CharField(max_length=30)
    email = models.EmailField(max_length=30,unique=True)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    dob = models.CharField(max_length=30)


class hirebook(models.Model):
    student_name=models.CharField(max_length=150 )
    book_name=models.CharField(max_length=100)
    book_id=models.IntegerField(default=0,blank=True)
    hire_date=models.CharField(max_length=100,blank=True)
    issu_date=models.DateField(max_length=100,blank=True)
    due=models.IntegerField()
    due2 = models.DateTimeField(auto_now_add=True, blank=True)


    