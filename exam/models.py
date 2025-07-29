from django.db import models

# from student.models import Student

class Exam(models.Model):
    exam_id = models.CharField(max_length=20, unique=True)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    is_public = models.BooleanField(default=False)
    time_limit = models.DurationField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_by = models.ForeignKey('administrator.Examiner', on_delete=models.CASCADE)


    def __str__(self):
        return self.exam_id

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.TextField()
    opt1 = models.CharField(max_length=200)
    opt2 = models.CharField(max_length=200)
    opt3 = models.CharField(max_length=200)
    opt4 = models.CharField(max_length=200)
    cans = models.CharField("Correct Answer", max_length=200)

    def __str__(self):
        return self.question_text

class ExamResult(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks = models.IntegerField()
    total_questions = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.loginid} - {self.exam.exam_id}"


from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name