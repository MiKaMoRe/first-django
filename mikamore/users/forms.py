from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from users.models import User
import re


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")
