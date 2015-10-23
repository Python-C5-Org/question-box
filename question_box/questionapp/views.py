from django.shortcuts import render, redirect

# from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import QuestionCreateForm
# from .models import Question
# Create your views here.


def index(request):
    return render(request, 'questionapp/index.html')


def new_answer(request):
    return render(request, 'questionapp/new_answer.html')


@login_required
def new_question(request):
    if request.method == 'POST':
        form = QuestionCreateForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.profile = request.user

            question.timestamp = datetime.now()
            question.save()
            return redirect('index')
    else:
        form = QuestionCreateForm()
    return render(request, 'questionapp/new_question.html',
                  {'form': form})
