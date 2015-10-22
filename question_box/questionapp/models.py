from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    profile = models.ForeignKey(User)
    timestamp = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    profile = models.ForeignKey(User)
    question = models.ForeignKey('Question')
    timestamp = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.text
