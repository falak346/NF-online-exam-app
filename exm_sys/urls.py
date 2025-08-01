"""
URL configuration for exm_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('admin_panel/', include('administrator.urls')),
#     path('', include('student.urls')),
#     path('exam/', include('exam.urls')),
# ]



# from django.contrib import admin
# from django.urls import path, include
# from administrator import views as administrator_views  # or whichever app has the view
from django.contrib import admin
from django.urls import path, include
from administrator import views as admin_views
from student import views as student_views


urlpatterns = [
    path('', admin_views.home, name='home'),  # 👈 Fixes "Page Not Found at /"
    path('admin/', admin.site.urls),
    path('admin_panel/', include('administrator.urls')),

    # These are direct views, so no need to include student.urls
    path('login/', student_views.student_login, name='student_login'),
    path('exam/', student_views.take_exam, name='take_exam'),
    path('result/', student_views.view_result, name='view_result'),
]
