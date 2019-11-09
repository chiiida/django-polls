from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.test import TestCase
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Choice, Question
import logging

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()
                                       ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

@login_required(login_url='/accounts/login/')
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def vote_count(id):
    """Return total votes for a given poll. id is poll id"""
    question = Question.objects.get(pk=id)
    total_votes = [choice.votes for choice in question.choice_set.all()]
    return sum(total_votes)

def find_polls_for_text(text):
    """Return list of Question objects for all polls containing some text"""
    return list(Question.objects.filter(question_text__contains=text))

def error_404_view(request, exception):
    data = {"name": "Chananchida"}
    return render(request,'polls/error_404.html', data)

def log_test(logger):
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('You have been warned')
    logger.error('This is an error')
    logger.critical('Something TERRIBLE happened.')