from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Student(models.Model):
    birthday = models.DateField()
    mobile_phone = models.CharField(max_length = 11)
    address = models.TextField()
    username = models.OneToOneField(User , on_delete=models.CASCADE)
    def __str__(self):
        return self.username.first_name



# @receiver(post_save, sender=User)
# def create_student(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(username=instance)

# @receiver(post_save, sender=User)
# def save_student(sender, instance, **kwargs):
#     instance.student.save()