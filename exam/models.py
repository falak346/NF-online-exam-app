from django.db import models

class Subject(models.Model):
    subname = models.CharField(max_length=100)

    def __str__(self):
        return self.subname

class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question_text = models.TextField()
    opt1 = models.CharField(max_length=200)
    opt2 = models.CharField(max_length=200)
    opt3 = models.CharField(max_length=200)
    opt4 = models.CharField(max_length=200)
    cans = models.CharField("Correct Answer", max_length=200)

    def __str__(self):
        return self.question_text
