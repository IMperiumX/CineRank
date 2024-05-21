# serializers.py
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator

from movies.models import (
    Collection,
    Genre,
    Language,
    Movie,
    ProductCompany,
    ProductCountry,
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["name", "poster_path", "backdrop_path"]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ["name", "iso_639_1", "english_name"]


class ProductCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCountry
        fields = ["name", "iso_3166_1"]


class ProductCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCompany
        fields = ["name", "logo_path", "origin_country"]


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)
    production_company = ProductCompanySerializer(many=True, read_only=True)
    production_country = ProductCountrySerializer(many=True, read_only=True)
    collection = CollectionSerializer(read_only=True)
    spoken_language = LanguageSerializer(many=True, read_only=True)

    # Custom serializer method field
    is_highly_rated = serializers.SerializerMethodField()

    def get_is_highly_rated(self, obj):
        return obj.vote_average >= 8.0

    # Custom validation example
    def validate_revenue(self, value):
        if value < 0:
            raise serializers.ValidationError("Revenue cannot be negative.")
        return value

    def validate(self, data):
        if data.get("budget") < 0:
            raise ValidationError({"budget": "Budget cannot be negative"})
        return data

    @transaction.atomic
    def create(self, validated_data):
        try:
            print("#" * 100)
            print(validated_data)
            instance = Movie.objects.create(**validated_data)
            return instance
        except Exception as e:
            raise ValidationError(str(e))

    class Meta:
        model = Movie
        fields = [
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
            "is_highly_rated",
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
        ]
        validators = [
            UniqueTogetherValidator(
                queryset=Movie.objects.all(), fields=["tmdb_id", "imdb_id"]
            ),
        ]
