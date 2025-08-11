from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PhotoContestSubmission

class PhotoContestSubmissionForm(forms.ModelForm):
    class Meta:
        model = PhotoContestSubmission
        fields = ['name', 'email', 'image']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
