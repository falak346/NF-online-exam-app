from django.shortcuts import render, redirect
from .models import Examiner, Batch, BatchMembership
from exam.models import Exam

def home(request):
    return render(request, 'home.html')

def select_login(request):
    return render(request, 'select_login.html')  # 👈 View for login choice

def select_signup(request):
    return render(request, 'select_signup.html')  # 👈 View for signup choice

def about_us(request):
    return render(request, 'about.html')

def examiner_login(request):
    if request.method == 'POST':
        ...
        request.session['examiner_id'] = examiner.id
        request.session['user_role'] = 'examiner'
        return redirect('ex_index')

def examiner_signup(request):
    if request.method == 'POST':
        ...
        Examiner.objects.create(...)
        return redirect('examiner_login')

def ex_index(request):
    examiner_id = request.session.get('examiner_id')
    ...
    return render(request, 'ex_index.html', {'batches': batches})

def batch_detail(request, batch_id):
    batch = Batch.objects.get(batch_id=batch_id)
    students = BatchMembership.objects.filter(batch=batch, approved=True)
    return render(request, 'batch_detail.html', {'batch': batch, 'students': students})
