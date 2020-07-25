from django.contrib import admin

from .models import my_user
from .models import answers
from .models import question

admin.site.register(my_user)
admin.site.register(answers)
admin.site.register(question)
