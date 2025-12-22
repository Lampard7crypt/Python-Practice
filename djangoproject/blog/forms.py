from django.forms import ModelForm
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']
