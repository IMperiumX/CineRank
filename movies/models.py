from django.db import models
from movies.api.tmdb import TMDBAPIMixin

from .managers import MovieQuerySet


class Image(models.Model):
    """Represents the image configuration from the TMDB API"""

    base_url = models.URLField(max_length=200)
    secure_base_url = models.URLField(max_length=200)
    backdrop_sizes = models.CharField(max_length=200)
    logo_sizes = models.CharField(max_length=200)
    poster_sizes = models.CharField(max_length=200)
    profile_sizes = models.CharField(max_length=200)
    still_sizes = models.CharField(max_length=200)


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
    images = models.ForeignKey(Image, on_delete=models.CASCADE)

    objects = MovieQuerySet.as_manager()


class Cast(models.Model):
    """Represents a cast member associated with a movie, including the actor's ID, character name, and name."""

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor_id = models.IntegerField()
    character_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)


class Crew(models.Model):
    """Represents a crew member associated with a movie, including the crew member's ID, job, and name."""

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    crew_id = models.IntegerField()
    job = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
