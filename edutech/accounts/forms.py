from django import forms
from .models import Student,Teacher

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
# from django.contrib.auth import password_validation
# from django.utils.translation import gettext_lazy as _




# Inheritense UserCreationForm method


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Enter Password...'}))

    password2 = forms.CharField(label='Confirm Password (again)',
                                widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Enter Password again...'}))

    class Meta:
        model = User
        fields = ['username',  'email']
        labels = {'email': 'Email :'}

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter  UserName'}),

            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email ID'}),

        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['user']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['user']
