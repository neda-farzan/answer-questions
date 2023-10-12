from django import forms
from .models import Answer, Question
from django.forms.fields import ChoiceField


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('name', 'email', 'body')


class AskForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('user', 'title', 'slug', 'subject', 'description')
    # name = forms.CharField(max_length=50)
    # email = forms.EmailField()
    # subject = forms.CharField(max_length=50)
    # title = forms.CharField(max_length=200)
    # description = forms.Textarea()


class SearchForm(forms.Form):
    query = forms.CharField()