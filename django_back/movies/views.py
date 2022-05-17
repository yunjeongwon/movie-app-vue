from asyncio import constants
from django.shortcuts import render,redirect
from movies.forms import MovieForm

from .models import Movie


def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html',context)


def db_create(request):
    if request.method == 'POST':
        print('POST')
        form = MovieForm(request.POST)
        # genres = Genre.objects.all()
        if form.is_valid():
            movie = form.save()
            return redirect('movies:index', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

