from dataclasses import field
from django import forms
from .models import ToiletInfo, Comment

class ToiletForm(forms.ModelForm):
    class Meta:
        model=ToiletInfo
        exclude = ('topen', 'tnumber',)
        labels = {
            'tname' : '화장실 이름',
            'tlocation' : '위치',
            'tlat' : '위도',
            'tlong' : '경도',
            'tbidget' : '비데',
            'tpaper' : '휴지',
            'tpassword' : '비밀번호',
            'tpublic' : '남여분리',
            'ttype' : '변기',
        }
        widgets ={
            'tname' : forms.TextInput(attrs={'class' : 'form-control'}),
            'tlocation' : forms.TextInput(attrs={'class' : 'form-control'}),
            'tlat' : forms.TextInput(attrs={'class' : 'form-control'}),
            'tlong' : forms.TextInput(attrs={'class' : 'form-control'}),
            'tpublic' : forms.NullBooleanSelect(attrs={'class' : 'form-select'}),
            'tbidget' : forms.NullBooleanSelect(attrs={'class' : 'form-control'}),
            'tpaper' : forms.NullBooleanSelect(attrs={'class' : 'form-select'}),
            'tpassword' : forms.NullBooleanSelect(attrs={'class' : 'form-select'}),
            'ttype' : forms.Select(attrs={'class' : 'form-select'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude = ()
        # field=['score']

