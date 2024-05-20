from django.contrib import admin

from .models import Genre, Collection, Language, ProductCountry, ProductCompany, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "poster_path", "backdrop_path")
    search_fields = ("name",)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "iso_639_1", "english_name")
    search_fields = ("name",)


@admin.register(ProductCountry)
class ProductCountryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "iso_3166_1")
    search_fields = ("name",)


@admin.register(ProductCompany)
class ProductCompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "logo_path", "origin_country")
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
        "release_date",
        "revenue",
        "runtime",
        "status",
        "tagline",
        "title",
        "video",
        "vote_average",
        "vote_count",
        "production_company",
        "production_country",
        "collection",
        "spoken_language",
        "genre",
    )
    list_filter = (
        "adult",
        "release_date",
        "video",
        "production_company",
        "production_country",
        "collection",
        "spoken_language",
        "genre",
    )
