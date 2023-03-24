from django import forms
from .models import masterSignup


class masterLoginForm(forms.Form):
    masterUserName = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Master Username','class':'InputLog'}),label='')
    masterPassword = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'InputLog'}),label='')

class masterSignupForm(forms.ModelForm):
    class Meta:
        model = masterSignup
        fields = '__all__'
        widgets={
            'firstname':forms.TextInput(attrs={'placeholder':'First name','class':'InputLog'}),
            'lastname':forms.TextInput(attrs={'placeholder':'Last name','class':'InputLog'}),
            'contact':forms.NumberInput(attrs={'placeholder':'Mobile no ','class':'InputLog'}),
            'email':forms.EmailInput(attrs={'placeholder':'Email','class':'InputLog'}),
            'address':forms.TextInput(attrs={'placeholder':'Address','class':'InputLog'}),
            'profile':forms.FileInput(attrs={'class':'InputLog'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter a username', 'class': 'InputLog'}),
        }
        labels = {
            'firstname' :'',
            'lastname' :'',
            'contact' :'',
            'email' :'',
            'address' :'',
            'profile' :'',
            'username': '',
        }

class masterSignupForm2(forms.Form):
    mainPassword = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'InputLog'}), label='')