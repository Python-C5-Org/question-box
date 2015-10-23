from django import forms

from .models import Answer, Question


class QuestionCreateForm(forms.ModelForm):
    title = forms.CharField(required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = Question
        fields = ('title', 'text')


class AnswerCreateForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = Answer
        fields = ('text',)
