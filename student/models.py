from django.db import models
# from exam.models import Subject

class Student(models.Model):
    name = models.CharField(max_length=100)
    enroll = models.CharField(max_length=20, unique=True)
    loginid = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


    def __str__(self):
        return self.loginid







