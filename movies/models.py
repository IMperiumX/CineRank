from django.db import models
from movies.api.tmdb import TMDBAPIMixin

from .managers import MovieQuerySet


class Movie(TMDBAPIMixin, models.Model):
    """Represents a movie with its basic information, such as title, release date, runtime, and genres."""

    tmdb_id = models.IntegerField(unique=True)
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=200)
    belongs_to_collection = models.CharField(max_length=200)
    budget = models.IntegerField()
    genres = models.CharField(max_length=200)
    homepage = models.CharField(max_length=200)
    imdb_id = models.CharField(max_length=200)
    origin_country = models.CharField(max_length=200)
    original_language = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    production_companies = models.CharField(max_length=200)
    production_countries = models.CharField(max_length=200)
    release_date = models.DateField()
    revenue = models.IntegerField()
    runtime = models.IntegerField()
    spoken_languages = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    tagline = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

    objects = MovieQuerySet.as_manager()
