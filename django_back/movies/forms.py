from django.forms import forms
from django import forms
from .models import Movie, Genre, Tag


class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title from-control',
                'maxlength' : 100,
                'placeholder': 'Title'
            }

        )
    )
    running_time = forms.IntegerField(
        label='Running_time',
        widget=forms.TextInput(
            attrs={
                'class' : 'from-control',
                'placeholder': 'running_time'
            }

        )
    )

    release_year = forms.IntegerField(
        label='Release_year',
        widget=forms.TextInput(
            attrs={
                'class' : 'from-control',
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

    genre_choice = (
        ('1','액션'),
        ('2','드라마'),
        ('3', '코미디'),
        ('4', '공포'),
        ('5', '로맨스'),
    )
    genre = forms.ModelMultipleChoiceField(
        label='Genre',
        queryset=Genre.objects.all(),
        # choices = genre_choice,
        widget=forms.SelectMultiple(),
    )
    tag_Choice =(
        ('화려함','화려함'),
    )
    tag = forms.ModelMultipleChoiceField(
        label='tag',
        queryset=Tag.objects.all(),
        # choices = tag_Choice,
        widget=forms.SelectMultiple()
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
        # fields = '__all__'
        exclude = ('wish_users',)