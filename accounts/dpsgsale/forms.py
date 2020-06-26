from django import forms
#from .models import *

class StudentForm(forms.Form):
    uname = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'size':30, 'placeholder': 'Create User Name'}))
    fname = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'size':30, 'placeholder': 'Enter First name'}))
    lname = forms.CharField(max_length=20,
                               widget=forms.TextInput(attrs={'size':30, 'placeholder': 'Enter Last Name'}))
    password = forms.CharField(max_length=20,
                               widget=forms.PasswordInput(attrs={'size':30, 'placeholder': 'Create Password'}))


class productForm(forms.Form):
    class_name = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'size': 30, 'placeholder': 'Enter Class'}))
    mobile = forms.CharField(max_length=10,
                            widget=forms.TextInput(attrs={'size': 30, 'placeholder': 'Enter Mobile No'}))
    price = forms.CharField(max_length=20,
                            widget=forms.NumberInput(attrs={'size': 30, 'placeholder': 'Enter rate'}))
    images = forms.ImageField()

"""class productForm(forms.ModelForm):

    class meta:
        fields = ['class_name', 'mobile', 'price', 'images']"""

