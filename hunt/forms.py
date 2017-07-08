from django import forms
from django.forms import TextInput
from .models import UserModel, LevelModel


class LoginForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['college', 'phone', 'email']
        widgets = {'college': TextInput(attrs={'class': 'form-control', 'placeholder': 'College'}),
                   'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone No'}),
                   'email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})}


class LevelForm(forms.ModelForm):

    class Meta:
        model = LevelModel
        fields = ['level_no', 'title', 'question_image', 'question_text', 'answer', 'placeholder_ans', ]
        labels = {'level_no': 'Level No', 'title': 'Question Title', 'question_text': 'Question Text',
                  'answer': 'Answer', 'placeholder_ans': 'Placeholder Answer', }

    def __init__(self, *args, **kwargs):
        super(LevelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
                self.fields[field].widget.attrs.update({'class': 'form-control'})




