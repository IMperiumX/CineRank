from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tmdb_id",
        "title",
        "original_title",
        "overview",
        "release_date",
        "runtime",
        "revenue",
        "budget",
        "genres",
        "languages",
        "production_companies",
        "production_countries",
        "spoken_languages",
        "status",
        "tagline",
        "video",
    )
    list_filter = ("release_date", "video")
