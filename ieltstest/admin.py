from django.contrib import admin

from django.contrib import admin
from .models import ReadingText, Question, Answer

admin.site.register(ReadingText)
admin.site.register(Question)
admin.site.register(Answer)