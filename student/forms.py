from django import forms
from .models import studentSignup, contact


class studentLoginForm(forms.Form):
    studentUserName = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Student Username', 'class': 'InputLog'}), label='')
    studentPassword = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'InputLog'}), label='')



class studentSignupForm(forms.ModelForm):
    class Meta:
        model = studentSignup
        fields = ['username','firstname','lastname','contact','email','address','profile']
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'InputLog'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'InputLog'}),
            'contact': forms.NumberInput(attrs={'placeholder': 'Mobile No', 'class': 'InputLog'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id', 'class': 'InputLog'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address', 'class': 'InputLog'}),
            'profile': forms.FileInput(attrs={'class': 'InputLog'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter a username', 'class': 'InputLog'}),
        }
        labels = {
            'firstname': '',
            'lastname': '',
            'contact': '',
            'email': '',
            'address': '',
            'profile': '',
            'username': '',
        }

class studentSignupForm2(forms.Form):
    # studentUserName = forms.CharField(max_length=100, widget=forms.TextInput(
    #     attrs={'placeholder': 'Student Username', 'class': 'InputLog'}), label='')

    studentPassword = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'InputLog'}), label='')


# contact form
class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name', 'class': 'InputLog'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'InputLog'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message', 'rows': 5, 'cols': 25, 'class': 'InputLogMess'}),
        }
        labels = {
            'name' : '',
            'email' : '',
            'message': '',
        }
