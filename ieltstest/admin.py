from django.contrib import admin
from .models import ReadingText, RQuestion, RAnswer, ListeningText, LQuestion, LAnswer, WritingText, WQuestion, WAnswer, ContactMessage, UniversityList

admin.site.register(ReadingText)
admin.site.register(RQuestion)
admin.site.register(RAnswer)

admin.site.register(ListeningText)
admin.site.register(LQuestion)
admin.site.register(LAnswer)

admin.site.register(WritingText)
admin.site.register(WQuestion)
admin.site.register(WAnswer)

admin.site.register(ContactMessage)

admin.site.register(UniversityList)