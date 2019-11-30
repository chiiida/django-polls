import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

from polls.models import Question, Choice, Vote

def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)
    
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class ChoiceModelTests(TestCase):

    def test_string_representation(self):
        choice = Choice(choice_text="Harry Potter")
        self.assertEqual('Harry Potter', str(choice))


class VoteModelTests(TestCase):

    def test_string_representation(self):
        question = create_question(question_text="Who is the best wizard?", days=-30)
        choice = Choice.objects.create(question=question, choice_text="Harry Potter")
        user = User.objects.create_user(username="muggle", password="harry101")
        vote = Vote.objects.create(question=question, choice=choice, user=user)
        self.assertEqual(
            'muggle: Who is the best wizard? – Harry Potter', str(vote))
