from django.shortcuts import render, redirect
from .models import Exam, ExamResult
from student.models import Student
from django.db.models import F

# PUBLIC Leaderboard
def public_leaderboard(request, exam_id):
    exam = Exam.objects.filter(exam_id=exam_id, is_public=True).first()
    if not exam:
        return render(request, '404.html', {'message': 'Exam not found or not public.'})

    results = ExamResult.objects.filter(exam=exam).select_related('student').order_by('-marks', 'submitted_at')
    current_student_id = request.session.get('student_id')

    return render(request, 'leaderboard_public.html', {
        'results': results,
        'exam': exam,
        'highlight_id': current_student_id
    })

# ASSIGNED Leaderboard
def assigned_leaderboard(request, exam_id):
    exam = Exam.objects.filter(exam_id=exam_id, is_public=False).first()
    if not exam:
        return render(request, '404.html', {'message': 'Assigned exam not found or not accessible.'})

    # Optional: restrict only to student who took the exam OR the examiner
    user_role = request.session.get('user_role')
    student_id = request.session.get('student_id')
    examiner_id = request.session.get('examiner_id')

    if user_role == 'student':
        attempted = ExamResult.objects.filter(student_id=student_id, exam=exam).exists()
        if not attempted:
            return redirect('st_index')
    elif user_role == 'examiner':
        if exam.created_by.id != examiner_id:
            return redirect('ex_index')
    else:
        return redirect('student_login')

    results = ExamResult.objects.filter(exam=exam).select_related('student').order_by('-marks', 'submitted_at')

    return render(request, 'leaderboard_assigned.html', {
        'results': results,
        'exam': exam,
        'highlight_id': student_id if user_role == 'student' else None
    })
