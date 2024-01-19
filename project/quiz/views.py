from django.shortcuts import render
from .models import Quiz

def index(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/index.html', {'quizzes': quizzes})