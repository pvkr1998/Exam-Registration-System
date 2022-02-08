from django.contrib import admin

# Register your models here.
from home.models import Examiner, Admin, Applicant

admin.site.register(Applicant)
admin.site.register(Examiner)
admin.site.register(Admin)
