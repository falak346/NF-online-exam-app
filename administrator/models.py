from django.db import models
from student.models import Student
class Admin(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.loginid

##admin (super user) ad examiner conflict can happen
class Examiner(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.png')

    def __str__(self):
        return self.loginid
class Batch(models.Model):
    batch_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    examiner = models.ForeignKey('Examiner', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class BatchMembership(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    requested_at = models.DateTimeField(auto_now_add=True)
