from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    """Redirects to polls index page."""
    return HttpResponseRedirect(reverse('polls:index'))