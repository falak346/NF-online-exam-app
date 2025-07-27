from django.shortcuts import render, HttpResponse

def test_exam_view(request):
    return HttpResponse("Exam app is working!")
