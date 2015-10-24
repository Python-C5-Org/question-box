from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import QuestionCreateForm, AnswerCreateForm
from .models import Question, Answer
# Create your views here.


def index(request):
    questions = Question.objects.all()
    return render(request, 'questionapp/index.html', {
        'questions': questions

    })


def question(request, question_id):
    question = Question.objects.get(pk=question_id)
    answers = question.answer_set.values()
    for answer in answers:
        answer['username'] = User.objects.get(pk=answer['profile_id']).username
    if request.method == 'POST':
        form = AnswerCreateForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.profile = request.user
            answer.timestamp = datetime.now()
            answer.question = question
            answer.save()
            return HttpResponseRedirect(reverse('question', kwargs={'question_id': question_id}))
    else:
        form = AnswerCreateForm()

    return render(request, 'questionapp/question.html', {'question': question,
                                                         'answers': answers,
                                                         'form': form})


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
