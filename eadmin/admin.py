from django.contrib import admin

# Register your models here.

from eadmin.models import Course, Exam, Enrollments

admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Enrollments)


