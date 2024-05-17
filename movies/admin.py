from django.contrib import admin

from .models import Image, Movie, Cast, Crew


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "base_url",
        "secure_base_url",
        "backdrop_sizes",
        "logo_sizes",
        "poster_sizes",
        "profile_sizes",
        "still_sizes",
    )


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
        "images",
    )
    list_filter = ("release_date", "video", "images")


@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = ("id", "movie", "actor_id", "character_name", "name")
    list_filter = ("movie",)
    search_fields = ("name",)


@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    list_display = ("id", "movie", "crew_id", "job", "name")
    list_filter = ("movie",)
    search_fields = ("name",)
