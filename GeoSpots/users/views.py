from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.views.generic.edit import CreateView

from .forms import ContactForm, CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


class Contact(CreateView):
    form_class = ContactForm
    template_name = 'users/contact.html'


@csrf_exempt
class PasswordReset(PasswordResetForm):
    form_class = PasswordResetForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/password_reset_form.html'