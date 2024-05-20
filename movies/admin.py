# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Genre, Collection, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "poster_path", "backdrop_path")
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tmdb_id",
        "imdb_id",
        "adult",
        "backdrop_path",
        "budget",
        "homepage",
        "origin_country",
        "original_language",
        "original_title",
        "overview",
        "popularity",
        "poster_path",
        "production_companies",
        "production_countries",
        "release_date",
        "revenue",
        "runtime",
        "spoken_languages",
        "status",
        "tagline",
        "title",
        "video",
        "vote_average",
        "vote_count",
        "collection",
        "genre",
    )
    list_filter = ("adult", "release_date", "video", "collection", "genre")
