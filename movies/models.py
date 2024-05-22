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


class Language(models.Model):
    """Represents a spoken language in the movie."""

    name = models.CharField(max_length=255)
    iso_639_1 = models.CharField(max_length=10)
    english_name = models.CharField(max_length=255)


class ProductCountry(models.Model):
    """Represents a production country of the movie."""

    name = models.CharField(max_length=255)
    iso_3166_1 = models.CharField(max_length=10)


class ProductCompany(models.Model):
    """Represents a production company of the movie."""

    name = models.CharField(max_length=255)
    logo_path = models.CharField(max_length=255)
    origin_country = models.CharField(max_length=255)


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
    release_date = models.DateField()
    revenue = models.IntegerField()
    runtime = models.IntegerField()
    status = models.CharField(max_length=50)
    tagline = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

    # Relationships
    production_company = models.ForeignKey(
        "movies.ProductCompany",
        on_delete=models.CASCADE,
        null=True,
    )
    production_country = models.ForeignKey(
        "movies.ProductCountry",
        on_delete=models.CASCADE,
        null=True,
    )
    collection = models.ForeignKey(
        "movies.Collection",
        on_delete=models.CASCADE,
        null=True,
    )
    spoken_language = models.ForeignKey(
        "movies.Language",
        on_delete=models.CASCADE,
        null=True,
    )
    genre = models.ForeignKey("movies.Genre", on_delete=models.CASCADE)

    objects = MovieQuerySet.as_manager()


class Rating(models.Model):
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )  # 1-5 star rating
    created_at = models.DateTimeField(auto_now_add=True)

    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            "movie",
            "user",
        )  # Ensure each user can rate a movie only once


class UserMoviePreference(models.Model):
    rating = models.FloatField()
    genre = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "movie")
        ordering = ("-created_at",)
