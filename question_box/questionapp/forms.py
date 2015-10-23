from django import forms

from .models import Answer, Question


class QuestionCreateForm(forms.Form):
    title = forms.CharField(required=True)
    text = forms.TextField(required=True)

    class Meta:
        model = Question
        fields = ('title', 'text')


class AnswerCreateForm(forms.Form):
    text = forms.TextField(required=True)

    class Meta:
        model = Answer
        fields = ('text',)
