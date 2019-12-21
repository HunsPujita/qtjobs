from django import forms
from jobs.models import *


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'


class CredForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'