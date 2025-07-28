from django.shortcuts import render, redirect
from .models import Student, ExamResult
from exam.models import Question, Subject

def student_login(request):
    if request.method == 'POST':
        loginid = request.POST['loginid']
        password = request.POST['password']
        student = Student.objects.filter(loginid=loginid, password=password).first()
        if student:
            request.session['student_id'] = student.id
            return redirect('take_exam')
        else:
            return render(request, 'student_login.html', {'error': 'Invalid credentials'})
    return render(request, 'student_login.html')

def student_signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        loginid = request.POST['loginid']
        password = request.POST['password']

        if Student.objects.filter(loginid=loginid).exists():
            return render(request, 'student_signup.html', {'error': 'Login ID already exists.'})
        
        Student.objects.create(name=name, loginid=loginid, password=password)
        return redirect('student_login')
    else:
        return render(request, 'student_signup.html')


def take_exam(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        student = Student.objects.get(id=request.session['student_id'])
        subject = Subject.objects.first()  # Later make dynamic
        total_q = len(questions)
        correct = 0
        for q in questions:
            selected = request.POST.get(str(q.id))
            if selected == q.cans:
                correct += 1
        ExamResult.objects.create(
            student=student,
            subject=subject,
            totalquestion=total_q,
            totalmarks=correct
        )
        return redirect('view_result')
    return render(request, 'take_exam.html', {'questions': questions})

def view_result(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(id=student_id)
    results = ExamResult.objects.filter(student=student)
    return render(request, 'result.html', {'results': results})
