from django.shortcuts import render, redirect
from . import models
from django.contrib import messages 
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm, SearchForm
from .models import ReadingText, RQuestion, RAnswer, ListeningText, LQuestion, LAnswer, WritingText, WQuestion, WAnswer, TestResult, UniversityList


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            form = ContactForm() 
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def guide(request):
    return render(request, 'guide.html')

def download(request):
    return render(request, 'download.html')

def search(request):
    results = []
    if request.method == 'GET':
        ielts_score = request.GET.get('ielts_score', None)
        if ielts_score:
            try:
                ielts_score = float(ielts_score)
                results = UniversityList.objects.filter(ielts_score_required=ielts_score)
            except ValueError:
                results = []
    return render(request, 'search.html', {'results': results})

def readingmore(request):
    return render(request, 'readingmore.html')

def listeningmore(request):
    return render(request, 'listeningmore.html')

def writingmore(request):
    return render(request, 'writingmore.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    return render(request, 'login.html')

@login_required
def profile(request):
    user_results = TestResult.objects.filter(user=request.user)
    return render(request, 'profile.html', {'results': user_results})

def skills(request):
    return render(request, 'skills.html')

@login_required
def reading_test(request, reading_text_id):
    reading_text = ReadingText.objects.get(id=reading_text_id)
    questions = RQuestion.objects.filter(reading_text=reading_text)

    if request.method == 'POST':
        score = 0
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer:
                answer = RAnswer.objects.get(id=user_answer)
                if answer.is_correct_for_reading:
                    score += 1
        TestResult.objects.create(user=request.user, skill='Reading', score=score)
        return redirect('profile')

    return render(request, 'reading_test.html', {'reading_text': reading_text, 'questions': questions})

@login_required
def listening_test(request, listening_text_id):
    listening_text = ListeningText.objects.get(id=listening_text_id)
    questions = LQuestion.objects.filter(listening_text=listening_text)

    if request.method == 'POST':
        score = 0
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer:
                answer = LAnswer.objects.get(id=user_answer)
                if answer.is_correct_for_listening:
                    score += 1
        TestResult.objects.create(user=request.user, skill='Listening', score=score)
        return redirect('profile')

    return render(request, 'listening_test.html', {'listening_text': listening_text, 'questions': questions})

@login_required
def writing_test(request, writing_text_id):
    writing_text = WritingText.objects.get(id=writing_text_id)
    questions = WQuestion.objects.filter(writing_text=writing_text)

    if request.method == 'POST':
        user_answer = request.POST.get('user_answer')
        # Here you can save the answer to the database or process it as needed
        # For now, we will just redirect to the profile
        TestResult.objects.create(user=request.user, skill='Writing', score=0)  # Adjust score logic as needed
        return redirect('profile')

    return render(request, 'writing_test.html', {'writing_text': writing_text, 'questions': questions})