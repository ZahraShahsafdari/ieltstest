from django.shortcuts import render
from .models import ReadingText

def reading(request):
    reading_texts = ReadingText.objects.all()
    return render(request, 'reading_test.html', {'reading_texts': reading_texts})


