from django import forms
from .models import Student
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(min_length=3,max_length=25)

    class Meta:
        model = User
        fields = ('username','password','first_name', 'last_name', 'email')
        

class StudentForm(forms.ModelForm):
    # address = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 10}))

    class Meta:
        model = Student
        fields = ('birthday', 'address', 'mobile_phone')
        widgets = {
        'address': forms.Textarea(attrs={'rows':4, 'cols':35}),
        'birthday' : forms.DateInput(attrs={'type': 'date'})
        }