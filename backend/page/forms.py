from django.forms import ModelForm
from django import forms
from .models import User

#Create User Form
class Form(forms.ModelForm):
    event_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'ex) Dinner'}))
    your_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'ex) William'}))
    your_email = forms.EmailField(label = "", widget=forms.EmailInput(attrs={'placeholder': 'ex) william@gmail.com'}))
    friend_name = forms.CharField(label ="", widget = forms.TextInput(attrs={'placeholder': 'ex) Olivia'}))
    friend_email = forms.EmailField(label = "", widget=forms.EmailInput(attrs={'placeholder': 'ex) olivia@hotmail.com'}))
    amount = forms.DecimalField(label = "", widget=forms.NumberInput(attrs={'placeholder': 'ex) 20'}))
    class Meta:
        model = User
        fields = ['event_name', 'your_name', 'your_email', 'friend_name', 'friend_email', 'amount']
        