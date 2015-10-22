from django.contrib import admin
from .models import Question, Answer
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    pass


class AnswerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
