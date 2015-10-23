from django.shortcuts import render, redirect

# from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import QuestionCreateForm, AnswerCreateForm
from .models import Question

# Create your views here.


def index(request):
    questions = Question.objects.all()
    return render(request, 'questionapp/index.html', {
        'questions': questions

    })


def question(request, question_id):
    question = Question.objects.get(pk=question_id)
    answers = question.answer_set.values()

    if request.method == 'POST':
        print('after post')
        form = AnswerCreateForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.profile = request.user
            answer.question = question_id
            answer.timestamp = datetime.now()
            answer.save()
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = AnswerCreateForm()
    return render(request, 'questionapp/question.html',
                  {'question': question,
                   'answers': answers,
                   'form': form})

    # return render(request, 'questionapp/question.html',
    #               {'question': question,
    #                'answers': answers})


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
