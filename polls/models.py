from django.db import models


# Create your models here.


class Poll(models.Model):
    title = models.CharField(max_length=200, blank=False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=False)
    description = models.TextField(verbose_name='Описание', blank=False)
    user_id = models.PositiveIntegerField(blank=True)
    is_finished = models.BooleanField(default=False)
    questions = models.ForeignKey('Question', on_delete=models.CASCADE)


class Question(models.Model):
    class TypeQuestion:
        Text = 1
        SingleSelection = 2
        MultiSelection = 3

    text = models.TextField(verbose_name='Текст вопроса', blank=False)
    type_question = models.TextField(choices=TypeQuestion)
    answer = models.ForeignKey('UserAnswer', on_delete=models.CASCADE)


class UserAnswer(models.Model):
    text_answer = models.TextField(blank=False)
