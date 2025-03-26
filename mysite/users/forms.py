from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    # Adding an additional field for email to the form.
    # forms.EmailField ensures that the input is a valid email address.
    email = forms.EmailField()

    # The Meta class is used to configure the form's behavior and specify its model and fields.
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']