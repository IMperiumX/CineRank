from django.db import models
from movies.api.tmdb import TMDBAPIMixin

from .managers import MovieQuerySet


class Movie(TMDBAPIMixin, models.Model):
    """Represents a movie with its basic information, such as title, release date, runtime, and genres."""

    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200)
    overview = models.TextField()
    release_date = models.DateField()
    runtime = models.IntegerField()
    revenue = models.IntegerField()
    budget = models.IntegerField()
    genres = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)
    production_companies = models.CharField(max_length=200)
    production_countries = models.CharField(max_length=200)
    spoken_languages = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    tagline = models.CharField(max_length=200)
    video = models.BooleanField()

    objects = MovieQuerySet.as_manager()
