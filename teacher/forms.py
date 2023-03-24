from django import forms
from .models import teacherSignup


class teacherLoginForm(forms.Form):
    teacherUserName = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Teacher Username','class':'InputLog'}),label='')
    teacherPassword = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'InputLog'}),label='')


class teacherSignupForm(forms.ModelForm):
    class Meta:
        model=teacherSignup
        fields= ['firstname','lastname','contact','email','address','profile','username'] 
    
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

class teacherSignupForm2(forms.Form):
    # studentUserName = forms.CharField(max_length=100, widget=forms.TextInput(
    #     attrs={'placeholder': 'Student Username', 'class': 'InputLog'}), label='')

    teacherPassword = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'InputLog'}), label='')