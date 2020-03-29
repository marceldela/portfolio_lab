from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms
from django.core.exceptions import ValidationError

from donation.models import Donation, Category


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='', max_length=150, widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    first_name = forms.CharField(label='', max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    last_name = forms.CharField(label='', max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Potwierdź hasło'}))



    def clean_email(self):
        email = self.cleaned_data['username'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError('Email already exists')
        return email

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].lower()
        r = User.objects.filter(last_name=last_name)
        return

    def clean_last_name(self):
        first_name = self.cleaned_data['first_name'].lower()
        r = User.objects.filter(first_name=first_name)
        return first_name

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            password=self.cleaned_data['password1']
        )
        return user



class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password'
        )
