from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from polls.models import Question, Choice


def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'polls/index.html', context)


def question_detail(request, pk):
    question = Question.objects.get(pk=pk)
    context = {
        'question': question,
    }
    return render(request, 'polls/question.html', context)


def vote(request, pk):
    if request.method == 'POST':
        question = Question.objects.get(pk=pk)
        try:
            choice_pk = request.POST.get('select')
        except Question.DoesNotExist:
            return redirect('question_index')
        try:
            choice = Choice.objects.get(pk=choice_pk)
            choice.votes += 1
            choice.save()
            question = choice.question
        except Question.DoesNotExist:
            return redirect('question_index')
        except MultiValueDictKeyError:
            print('KeyError!')
        except Choice.DoesNotExist:
            print('Choice.DoesNotExist!')
        return redirect('question_detail', pk=question.pk)

    return redirect('Permission denied', status=403)
