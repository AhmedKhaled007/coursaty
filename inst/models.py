from django.db import models
from datetime import date
# Create your models here.


class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField('Birthday')
    email = models.EmailField()
    photo = models.ImageField(upload_to = 'profile' , blank=True)
    summary = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def age(self):
        return date.today() - self.date_of_birth

