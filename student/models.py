from django.db import models
from exam.models import Subject

class Student(models.Model):
    enroll = models.CharField(max_length=20)
    loginid = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.loginid

class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    totalmarks = models.IntegerField()
    totalquestion = models.IntegerField()

    def __str__(self):
        return f"{self.student.loginid} - {self.subject.subname}"
