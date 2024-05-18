from api.tmdb import TMDBAPIMixin
from django.db import models

from .models import Cast, Crew


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
        # Update cast and crew data
        movie.cast.set(
            [
                Cast.objects.get_or_create(
                    actor_id=cast["actor_id"],
                    character_name=cast["character_name"],
                    defaults={"name": cast["name"]},
                )[0]
                for cast in movie_data["credits"]["cast"]
            ]
        )
        movie.crew.set(
            [
                Crew.objects.get_or_create(
                    crew_id=crew["id"], job=crew["job"], defaults={"name": crew["name"]}
                )[0]
                for crew in movie_data["credits"]["crew"]
            ]
        )
        return movie
