from django.contrib import admin

# Register your models here.
from examiner.models import Results,questions,responses

admin.site.register(Results)
admin.site.register(questions)
admin.site.register(responses)
