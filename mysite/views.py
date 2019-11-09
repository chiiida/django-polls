from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login


def index(request):
    """Redirects to polls index page."""
    return HttpResponseRedirect(reverse('polls:index'))

# def signup(request):
#     """Register a new user."""
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_passwd = form.cleaned_data.get('password')
#             user = authenticate(username=username,password=raw_passwd)
#             login(request, user)
#             return redirect('polls')
#         # what if form is not valid?
#         # we should display a message in signup.html
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})