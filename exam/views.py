from django.shortcuts import HttpResponse

def test_exam_view(request):
    return HttpResponse("Exam app is working!")
