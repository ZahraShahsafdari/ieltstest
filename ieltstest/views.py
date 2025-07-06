from django.shortcuts import render, redirect
from . import models
from .models import ReadingText, ListeningText, WritingText, WAnswer

def index(request):
    return render(request, 'index.html')


def reading(request):
    reading_texts = ReadingText.objects.prefetch_related('rquestions__ranswers').all()
    return render(request, 'reading_test.html', {'reading_texts': reading_texts})

def listening(request):
    listening_test = ListeningText.objects.prefetch_related('lquestions__lanswers').first()
    if listening_test is None:
        questions = []
    else:
        questions = listening_test.lquestions.all()  # Get related questions
    return render(request, 'listening_test.html', {
        'listening_test': listening_test,
        'questions': questions
    })

def writing(request):
    writing_text = WritingText.objects.first()
    if request.method == 'POST':
        answer_text = request.POST.get('user_answer')
        if answer_text and writing_text:
            WAnswer.objects.create(wquestion=None, answer_text=answer_text)
            return redirect('writing_test')
    return render(request, 'writing_test.html', {'writing_text': writing_text})