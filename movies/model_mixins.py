import requests
from requests.exceptions import RequestException

from django.conf import settings
from .exceptions import APIError, AuthenticationError, NotFoundError, ConnectionError


class TMDBAPIMixin:
    def __init__(self, api_key: str, api_url: str | None = None):
        self.api_key = api_key or settings.TMDB_API_KEY
        self.api_url = api_url or "https://api.themoviedb.org/3"

    def _make_request(self, method: str, endpoint: str, params: dict = None) -> dict:
        try:
            response = requests.request(
                method, f"{self.api_url}/{endpoint}", params=params
            )
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            return response.json()
        except RequestException as e:
            self._handle_request_error(e)

    def _handle_request_error(self, e: RequestException) -> None:
        if e.response is not None:
            status_code = e.response.status_code
            if status_code == 401:
                raise AuthenticationError("Invalid API key")
            elif status_code == 404:
                raise NotFoundError("Resource not found")
            else:
                raise APIError(f"API error: {e.response.text}")
        else:
            raise ConnectionError("Failed to connect to API")

    def get_movie(self, movie_id: int) -> dict:
        return self._make_request("GET", f"movie/{movie_id}", {"api_key": self.api_key})

    def search_movies(self, query: str) -> list[dict]:
        response = self._make_request(
            "GET", "search/movie", {"api_key": self.api_key, "query": query}
        )
        return response["results"]

    def get_genres(self) -> list[dict]:
        return self._make_request("GET", "genre/movie/list", {"api_key": self.api_key})

    def get_genre(self, genre_id: int) -> dict:
        return self._make_request("GET", f"genre/{genre_id}", {"api_key": self.api_key})

    def get_movie_credits(self, movie_id: int) -> dict:
        return self._make_request(
            "GET", f"movie/{movie_id}/credits", {"api_key": self.api_key}
        )

    def get_movie_reviews(self, movie_id: int) -> list[dict]:
        response = self._make_request(
            "GET", f"movie/{movie_id}/reviews", {"api_key": self.api_key}
        )
        return response["results"]

    def get_movie_images(self, movie_id: int) -> list[dict]:
        response = self._make_request(
            "GET", f"movie/{movie_id}/images", {"api_key": self.api_key}
        )
        return response["backdrops"] + response["posters"]

    def get_person(self, person_id: int) -> dict:
        return self._make_request(
            "GET", f"person/{person_id}", {"api_key": self.api_key}
        )

    def search_people(self, query: str) -> list[dict]:
        response = self._make_request(
            "GET", "search/person", {"api_key": self.api_key, "query": query}
        )
        return response["results"]

    def get_tv_show(self, tv_show_id: int) -> dict:
        return self._make_request("GET", f"tv/{tv_show_id}", {"api_key": self.api_key})

    def search_tv_shows(self, query: str) -> list[dict]:
        response = self._make_request(
            "GET", "search/tv", {"api_key": self.api_key, "query": query}
        )
        return response["results"]
