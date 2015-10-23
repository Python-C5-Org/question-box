from django.contrib import admin
from .models import Question, Answer
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'profile', 'timestamp']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'text', 'profile', 'timestamp']

admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
