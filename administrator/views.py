from django.shortcuts import render, redirect
from .models import Admin

def home(request):
    return render(request, 'home.html')

def select_login(request):
    return render(request, 'select_login.html')  # 👈 View for login choice

def select_signup(request):
    return render(request, 'select_signup.html')  # 👈 View for signup choice

from .models import Admin  # already imported

def admin_signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        loginid = request.POST['loginid']
        password = request.POST['password']

        if Admin.objects.filter(loginid=loginid).exists():
            return render(request, 'admin_signup.html', {'error': 'Login ID already exists.'})

        Admin.objects.create(name=name, loginid=loginid, password=password)
        return redirect('admin_login')

    return render(request, 'admin_signup.html')


def admin_login(request):
    if request.method == 'POST':
        loginid = request.POST['loginid']
        password = request.POST['password']
        if Admin.objects.filter(loginid=loginid, password=password).exists():
            return redirect('admin_dashboard')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials'})
    return render(request, 'admin_login.html')

def about_us(request):
    return render(request, 'about.html')


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


