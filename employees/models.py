from django.db import models

# Create your models here.

class Employees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #when the records is first created
    updated_at = models.DateTimeField(auto_now=True) # to records when any changes made to this field   

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' / ' + self.designation
