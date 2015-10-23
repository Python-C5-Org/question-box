from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import QuestionCreateForm
from .models import Question
# Create your views here.


class CreateQuestion(CreateView):
    model = Question
    fields = ['title', 'text']

    @login_required
    def get(self, request):
        return super().get(request)

    @login_required
    def post(self, request):
        title = request.POST['title']
        text = request.POST['text']

        Question.objects.create(title=title, text=text,
                                profile=request.user.profile,
                                timestamp=datetime.utcnow())

    return render(request, 'questionapp/new_question.html', {'form': form})


# @login_required
# def add_bookmark(request):
#     if request.method == 'POST':
#         form = BookmarkForm(request.POST)
#         if form.is_valid():
#             bookmark = form.save(commit=False)
#             bookmark.user = request.user
#             bookmark.generate_short()
#             bookmark.modified = datetime.now()
#             bookmark.save()
#             return redirect('recent')
#     else:
#         form = BookmarkForm()
#     return render(request, 'crisco/add_bookmark.html',
#                   {'form': form})
