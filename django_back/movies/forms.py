from django.forms import forms
from django import forms
from .models import Movie

class MovieForm(forms.modelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title from-control',
                'maxlength' : 20,
                'placeholder': 'Title'
            }

        )
    )
    running_time = forms.CharField(
        label='Running_time',
        widget=forms.TextInput(
            attrs={
                'class' : 'from-control',
                'maxlength' : 5,
                'placeholder': 'running_time'
            }

        )
    )

    release_year = forms.CharField(
        label='Release_year',
        widget=forms.TextInput(
            attrs={
                'class' : 'from-control',
                'maxlength' : 10,
                'placeholder': 'release_year'
            }

        )
    )
    age_choice = (
        ('10대 이하','10대 이하'),
        ('10대','10대'),
        ('20대','20대'),
        ('30대','30대'),
        ('40대','40대'),
        ('50대 이상','50대 이상'),

    )
    age_range = forms.ChoiceField(        
        label='Age_range',
        choices = age_choice,
        widget=forms.Select(
            attrs={
                'class' : 'form-control'
            }

        )
    )

    genere_choice = (
        ('액션','액션'),
        ('드라마','드라마'),
        ('코미디', '코미디'),
        ('공포', '공포'),
        ('로맨스', '로맨스'),
    )
    genere = forms.ChoiceField(        
        label='Genre',
        choices = genere_choice,
        widget=forms.RadioSelect(
            attrs={
                'class' : 'form-control'
            }

        )
    )
    tag_Choice =(
        ('화려함','화려함'),
    )
    tag = forms.ChoiceField(        
        label='tag',
        choices = tag_Choice,
        widget=forms.RadioSelect(
            attrs={
                'class' : 'form-control'
            }

        )
    )
    poster_url = forms.CharField(
        label='Poster url',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Poster url'
            }

        )
    )
    trailer_url = forms.CharField(
        label='Trailer_url',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'trailer_url'
            }

        )
    )
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Description'
            }

        )
    )

    class Meta:
        model = Movie
        fields = '__all__'