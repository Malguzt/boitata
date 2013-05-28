#encoding:utf-8

from django.forms import ModelForm
from django import forms
from party.models import Party, Character, Narration, Scene

class PartyForm(ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Titulo'}))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'Descripción'}))
    class Meta:
        model = Party
        fields = ('title', 'description')

class CharacterForm(ModelForm):
    class Meta:
        model = Character

class NarrationForm(ModelForm):
    class Meta:
        model = Narration

class SceneForm(ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Titulo'}))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'Descripción'}))
    class Meta:
        model = Scene
        fields = ('title', 'description')

class CharacterForm(ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Su nombre'}))
    history = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'Su historia'}))
    class Meta:
        model = Character
        fields = ('name', 'history')