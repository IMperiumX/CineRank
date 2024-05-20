from django.db import models

from movies.api.tmdb import TMDBAPIMixin


class MovieQuerySet(models.QuerySet):
    def fetch_and_update(self, tmdb_id: int):
        movie_data = TMDBAPIMixin.fetch_movie_by_id(tmdb_id)
        movie, created = self.model.objects.update_or_create(
            tmdb_id=tmdb_id,
            defaults={
                "adult": movie_data["adult"],
                "backdrop_path": movie_data["backdrop_path"],
                "belongs_to_collection": movie_data["belongs_to_collection"],
                "budget": movie_data["budget"],
                "genres": movie_data["genres"],
                "homepage": movie_data["homepage"],
                "imdb_id": movie_data["imdb_id"],
                "origin_country": movie_data["origin_country"],
                "original_language": movie_data["original_language"],
                "original_title": movie_data["original_title"],
                "overview": movie_data["overview"],
                "popularity": movie_data["popularity"],
                "poster_path": movie_data["poster_path"],
                "production_companies": movie_data["production_companies"],
                "production_countries": movie_data["production_countries"],
                "release_date": movie_data["release_date"],
                "revenue": movie_data["revenue"],
                "runtime": movie_data["runtime"],
                "spoken_languages": movie_data["spoken_languages"],
                "status": movie_data["status"],
                "tagline": movie_data["tagline"],
                "title": movie_data["title"],
                "video": movie_data["video"],
                "vote_average": movie_data["vote_average"],
                "vote_count": movie_data["vote_count"],
            },
        )
        return movie

    def get(self, *args, **kwargs):
        """
        Override the default get method to fetch the movie from the API if it doesn't exist in the database.
        """
        try:
            return super().get(*args, **kwargs)
        except self.model.DoesNotExist:
            tmdb_id = kwargs.get("tmdb_id")
            if tmdb_id:
                return self.fetch_and_update(tmdb_id)
            raise
