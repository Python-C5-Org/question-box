from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import QuestionCreateForm
from .models import Question
# Create your views here.


def index(request):
    questions = Question.objects.all()
    return render(request, 'questionapp/index.html', {
        'questions': questions

    })


def new_answer(request):
    return render(request, 'questionapp/new_answer.html')


def question(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'questionapp/question.html', {'question': question})


@login_required
def new_question(request):
    if request.method == 'POST':
        form = QuestionCreateForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.profile = request.user
            question.timestamp = datetime.now()
            question.save()
            return HttpResponseRedirect(reverse('question', kwargs={'question_id': question.id}))
    else:
        form = QuestionCreateForm()

    return render(request, 'questionapp/new_question.html',
                  {'form': form})
