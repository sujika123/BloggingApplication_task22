from django import forms
from django.contrib.auth.forms import UserCreationForm

from blogapp.models import Login, userlogin, blog


class DateInput(forms.DateInput):
    input_type = "date"

class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget = forms.PasswordInput,label = 'password')
    password2 = forms.CharField(widget = forms.PasswordInput, label = 'Confirm password')
    class Meta:
        model = Login
        fields = ('username','password1','password2')


class userloginform(forms.ModelForm):

    class Meta:
        model = userlogin
        fields = ('name','email')

class bloggingform(forms.ModelForm):
    class Meta:
        model = blog
        fields = ('title','content','author')
