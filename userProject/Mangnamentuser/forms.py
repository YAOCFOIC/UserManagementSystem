from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .validation import validate_email_unique, validate_username_unique, validate_passwords_match
from account.models import CustomUser

class CustomerCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','password1','password2','phone','address']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        validate_email_unique(email)
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        validate_username_unique(username)
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        validate_passwords_match(password1, password2)
        return cleaned_data

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email','phone','address')
