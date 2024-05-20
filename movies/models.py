from django.db import models
from movies.api.tmdb import TMDBAPIMixin

from .managers import MovieQuerySet


class Genre(models.Model):
    name = models.CharField(max_length=255)


class Collection(models.Model):
    """Represents a collection of movies."""

    name = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255)
    backdrop_path = models.CharField(max_length=255)


class Movie(TMDBAPIMixin, models.Model):
    """Represents a movie with its basic information, such as title, release date, runtime, and genres."""

    tmdb_id = models.IntegerField(unique=True)
    imdb_id = models.CharField(max_length=255)
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=255)
    budget = models.IntegerField()
    homepage = models.CharField(max_length=255)
    origin_country = models.CharField(max_length=255)
    original_language = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=255)
    production_companies = models.CharField(max_length=255)
    production_countries = models.CharField(max_length=255)
    release_date = models.DateField()
    revenue = models.IntegerField()
    runtime = models.IntegerField()
    spoken_languages = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    tagline = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

    # Relationships
    collection = models.ForeignKey(
        "movies.Collection",
        on_delete=models.CASCADE,
        null=True,
    )
    genre = models.ForeignKey("movies.Genre", on_delete=models.CASCADE)

    objects = MovieQuerySet.as_manager()
