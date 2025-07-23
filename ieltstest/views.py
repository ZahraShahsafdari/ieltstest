from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages 
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm, SearchForm
from django.core.exceptions import MultipleObjectsReturned
from .models import ReadingText, RQuestion, RAnswer, ListeningText, LQuestion, LAnswer, WritingText, WQuestion, WAnswer, TestScore, UniversityList

def index(request):
    return render(request, 'index.html')

def signup(request, email):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = email  # Set the email from the previous step
            user.save()
            login(request, user)  # Log the user in after signing up
            return redirect('ieltstest:profile')  # Redirect to profile page
        else:
            print("Form errors:", form.errors)  # Print form errors for debugging
    else:
        form = CustomUserCreationForm(initial={'email': email})
    return render(request, 'signup.html', {'form': form, 'email': email})

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            login(request, user)
            return redirect('ieltstest:profile')  # Redirect to profile page
        except User.DoesNotExist:
            return redirect('ieltstest:signup', email=email)  # Redirect to signup view with email
        except MultipleObjectsReturned:
            # Handle the case where multiple users exist with the same email
            print("Multiple users found with the same email. Please contact support.")
            # Optionally, redirect to an error page or show a message
            return redirect('ieltstest:signin')  # Redirect back to signin or show an error message
    return render(request, 'signin.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('ieltstest:signin')  # Redirect to signin page if not logged in
    scores = TestScore.objects.filter(user=request.user)
    return render(request, 'profile.html', {'scores': scores})

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
        TestScore.objects.create(user=request.user, skill='Reading', score=score)
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
        TestScore.objects.create(user=request.user, skill='Listening', score=score)
        return redirect('profile')
    return render(request, 'listening_test.html', {'listening_text': listening_text, 'questions': questions})

@login_required
def writing_test(request, writing_text_id):
    writing_text = WritingText.objects.get(id=writing_text_id)
    questions = WQuestion.objects.filter(writing_text=writing_text)
    if request.method == 'POST':
        user_answer = request.POST.get('user_answer')
        TestScore.objects.create(user=request.user, skill='Writing', score=0)
        return redirect('profile')
    return render(request, 'writing_test.html', {'writing_text': writing_text, 'questions': questions})