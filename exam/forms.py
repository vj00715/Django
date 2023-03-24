from django import forms
from .models import courses, Question

class coursesForm(forms.ModelForm):
    class Meta:
        model = courses
        fields = '__all__'
        widgets = {
            'courseName':forms.TextInput(attrs={'class':'InputLog','placeholder':'Enter Course Name'}),
            'questionMarks':forms.TextInput(attrs={'class':'InputLog','placeholder':'Enter Course Marks'}),
            'totalQuestion':forms.TextInput(attrs={'class':'InputLog','placeholder':'Enter Total Question'}),
        }
        labels = {
            'courseName': '',
            'questionMarks':'',
            'totalQuestion':'',
        }

class questionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        # ['course','question','option1','option2','option3','option4','answer']
        widgets = {
            'course':forms.Select(attrs={'class':'InputLog'}),
            'courseQuestion':forms.TextInput(attrs={'placeholder':'Enter Course Name Same As Above Dropdown Menu','class':'InputLog'}),
            'question':forms.TextInput(attrs={'placeholder':'Enter Question','class':'InputLog'}),
            'option1':forms.TextInput(attrs={'placeholder':'Enter Option 1','class':'InputLog'}),
            'option2':forms.TextInput(attrs={'placeholder':'Enter Option 2','class':'InputLog'}),
            'option3':forms.TextInput(attrs={'placeholder':'Enter Option 3','class':'InputLog'}),
            'option4':forms.TextInput(attrs={'placeholder':'Enter Option 4','class':'InputLog'}),
            'answer':forms.TextInput(attrs={'placeholder':'Enter Answer','class':'InputLog'}),
        }
        labels = {
            'course': '',
            'courseQuestion':'',
            'marks': '',
            'question': '',
            'option1': '',
            'option2': '',
            'option3': '',
            'option4': '',
            'answer': '',
        }



