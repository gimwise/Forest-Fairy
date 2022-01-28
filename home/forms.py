from dataclasses import field
from django import forms
from .models import ToiletInfo, Comment

class ToiletForm(forms.ModelForm):
    class Meta:
        model=ToiletInfo
        field='__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        field=['score']