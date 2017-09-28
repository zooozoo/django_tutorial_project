from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateTimeField(blank=True)

    def __str__(self):
        return f'설문조사 ({self.title})'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    title = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} (설문:{self.question.title}'