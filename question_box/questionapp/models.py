from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    profile = models.ForeignKey(User)
    timestamp = models.DateTimeField(blank=True, null=True)
    score = SmallIntegerField()

    def __str__(self, title, score):
        self.title = title
        self.score = 0


class Answer(models.Model):
    text = models.TextField()
    profile = models.ForeignKey(User)
    question = models.ForeignKey('Question')
    timestamp = models.DateTimeField(null=True)
    score = SmallIntegerField()

    def __str__(self, text, score):
        self.text = text
        self.score = 0


class UserScore(models.Model):
    user_score = SmallIntegerField()

    def __str__(self):
        return self.id


class AnswerScore(models.Model):
    answer_id = models.ForeignKey(Profile)
    answer_score = SmallIntegerField()

    def __str__(self):
        return self.id


class QuestionScore(models.Model):
    question_id = models.ForeignKey(Profile)
    question_score = SmallIntegerField()

    def __str__(self):
        return self.id
