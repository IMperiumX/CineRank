from django.db import models

from movies.api.tmdb import TMDBAPIMixin


class MovieQuerySet(models.QuerySet):
    def fetch_and_update(self, tmdb_id: int):
        movie_data = TMDBAPIMixin.fetch_movie_by_id(tmdb_id)
        movie, created = self.model.objects.update_or_create(
            tmdb_id=tmdb_id,
            defaults={
                "title": movie_data["title"],
                "overview": movie_data["overview"],
                # Update other fields as needed
            },
        )
        return movie
