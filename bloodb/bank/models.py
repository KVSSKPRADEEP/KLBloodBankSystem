from django.db import models

# Create your models here.

class Registeration(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    b_groups = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    name = models.CharField(max_length=100)
    blood_group = models.CharField(choices=b_groups, max_length=20)
    email = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    age = models.CharField(max_length=15)
    gender = models.CharField(choices=gender_choices, max_length=100)

    def __str__(self):
        return self.name
