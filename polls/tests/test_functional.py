import datetime
from django.utils import timezone
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from django.urls import reverse

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from typing import List

from polls.tests.test import get_links
from polls.models import Question, Choice


def create_question(question_text, days):
   """
   Create a question with the given `question_text` and published the
   given number of `days` offset to now (negative for questions published
   in the past, positive for questions that have yet to be published).
   """
   time = timezone.now() + datetime.timedelta(days=days)
   return Question.objects.create(question_text=question_text, pub_date=time)


class PollsFunctionalTest(LiveServerTestCase):
   url = 'https://cpske.github.io/ISP/'
   username = 'testuser'
   password = '12345678test'

   def setUp(self):
      options = webdriver.ChromeOptions()
      options.add_argument('--headless')
      self.browser = webdriver.Chrome(chrome_options=options)
      super(PollsFunctionalTest, self).setUp()

   def tearDown(self):
      self.browser.quit()
      super(PollsFunctionalTest, self).tearDown()

   def setup_user(self):
      User.objects.create_user(self.username, password=self.password)
      self.browser.get(self.live_server_url + '/accounts/login/')
      self.browser.find_element_by_id('id_username').send_keys(self.username)
      self.browser.find_element_by_id('id_password').send_keys(self.password)
      self.browser.find_element_by_id('login-btn').click()

   def test_contains_in_heading(self):
      self.browser.get(self.live_server_url + '/polls/')
      tag_element = self.browser.find_element_by_tag_name('h1')
      self.assertEqual('Polls', tag_element.text)
   
   def test_question_on_index(self):
      pass
      # self.browser.get(self.live_server_url + "polls:index")
