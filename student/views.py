from django.shortcuts import render, redirect
from .models import Student
from exam.models import Exam, ExamResult, Question
from django.utils import timezone
import random
from django.http import HttpResponse

def student_login(request):
    if request.method == 'POST':
        loginid = request.POST['loginid']
        password = request.POST['password']
        student = Student.objects.filter(loginid=loginid, password=password).first()
        if student:
            request.session['student_id'] = student.id
            request.session['user_role'] = 'student'
            return redirect('st_index')
        else:
            return render(request, 'student_login.html', {'error': 'Invalid credentials'})
    return render(request, 'student_login.html')

def student_signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        enroll = request.POST['enroll']
        loginid = request.POST['loginid']
        password = request.POST['password']
        email = request.POST['email']
        contact = request.POST['contact']

        if Student.objects.filter(loginid=loginid).exists():
            return render(request, 'student_signup.html', {'error': 'Login ID already exists.'})

        Student.objects.create(name=name, enroll=enroll, loginid=loginid, password=password, email=email, contact=contact)
        return redirect('student_login')
    return render(request, 'student_signup.html')

def st_index(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')
    open_exams = Exam.objects.filter(is_public=True)
    return render(request, 'st_index.html', {'exams': open_exams})

def attempt_exam(request, exam_id):
    student = Student.objects.get(id=request.session['student_id'])
    exam = Exam.objects.get(exam_id=exam_id)

    if ExamResult.objects.filter(student=student, exam=exam).exists():
        return HttpResponse("You already attempted this exam.")

    now = timezone.now()
    if not (exam.start_date <= now <= exam.end_date):
        return HttpResponse("This exam is not currently available.")

    if request.method == 'POST':
        total = 0
        questions = Question.objects.filter(exam=exam)
        for q in questions:
            selected = request.POST.get(str(q.id))
            if selected == q.cans:
                total += 1
        ExamResult.objects.create(
            student=student,
            exam=exam,
            marks=total,
            total_questions=questions.count()
        )
        return redirect('student_result', exam_id=exam_id)

    questions = list(Question.objects.filter(exam=exam))
    random.shuffle(questions)
    return render(request, 'exam_page.html', {'questions': questions, 'exam': exam})

def student_result(request, exam_id):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')
    student = Student.objects.get(id=student_id)
    result = ExamResult.objects.get(student=student, exam__exam_id=exam_id)
    return render(request, 'student_result.html', {'result': result})
