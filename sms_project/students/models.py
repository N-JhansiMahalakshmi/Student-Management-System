from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='students/', null=True, blank=True)

    def __str__(self):
        return self.full_name