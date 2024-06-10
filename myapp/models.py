from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    included_choices=(('IT','IT'),
                      ('Non IT','Non IT'),
                      ('mobiles phones','mobile phones'))
    type= models.CharField(max_length=100,choices=included_choices)
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

class reg_user(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)