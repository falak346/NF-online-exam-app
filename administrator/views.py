from django.shortcuts import render, redirect
from .models import Admin

def admin_login(request):
    # if request.method == 'POST':
    #     loginid = request.POST['loginid']
    #     password = request.POST['password']
    #     if Admin.objects.filter(loginid=loginid, password=password).exists():
    #         return redirect('admin_dashboard')
    #     else:
    #         return render(request, 'admin_login.html', {'error': 'Invalid credentials'})
    return render(request, 'admin_login.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


