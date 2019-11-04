from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout


def index(request):
    """Redirects to polls index page."""
    return HttpResponseRedirect(reverse('polls:index'))
    