import os
import django
from collections import defaultdict

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exm_sys.settings')
django.setup()

from student.models import Student
from django.db import connection

# Safely ignore profile_image column if it doesn't exist yet
def column_exists(model, column_name):
    with connection.cursor() as cursor:
        table = model._meta.db_table
        cursor.execute(f"PRAGMA table_info({table})")
        return any(col[1] == column_name for col in cursor.fetchall())

if not column_exists(Student, 'profile_image'):
    print("⚠️ Skipping profile_image check – column does not exist yet.")

seen = set()
for student in Student.objects.all().only('id', 'enroll', 'name'):  # avoid selecting profile_image
    if student.enroll in seen:
        original = student.enroll
        student.enroll = f"{original}_{student.id}"
        print(f"Renamed enroll: {original} → {student.enroll}")
        student.save(update_fields=['enroll'])  # avoid touching image field
    else:
        seen.add(student.enroll)

print("✅ All duplicate enroll IDs fixed.")
