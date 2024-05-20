from django.db import models
from django.db.models import (
    ExpressionWrapper,
    F,
    FloatField,
    Max,
    Min,
    Subquery,
    Value,
)
from django.db.models.functions import Cast


class MovieQuerySet(models.QuerySet):
    """
    score = (popularity_weight * normalized_popularity) +
        (vote_average_weight * normalized_vote_average) +
        (vote_count_weight * normalized_vote_count) +
        (revenue_weight * normalized_revenue) +
        (recency_weight * normalized_recency) +
        (user_rating_weight * normalized_user_rating) +
        (genre_preference_weight * genre_preference_score)
    using django queryset

    """

    def get_ranking(
        self,
        popularity_weight=0.1,
        vote_average_weight=0.2,
        vote_count_weight=0.1,
        revenue_weight=0.1,
        recency_weight=0.1,
        user_rating_weight=0.1,
        genre_preference_weight=0.3,
    ):
        # Normalizing popularity
        popularity = self._normalize("popularity")
        # Normalizing vote_average
        vote_average = self._normalize("vote_average")
        # Normalizing vote_count
        vote_count = self._normalize("vote_count")

        # Normalizing revenue
        revenue = self._normalize("revenue")
        # Normalizing recency
        recency = self._normalize("release_date")
        # Normalizing user_rating
        user_rating = self._normalize("user_rating")
        # Calculating genre preference score
        genre_preference_score = self._get_genre_preference_score()
        # Calculating ranking score
        return (
            popularity_weight * popularity
            + vote_average_weight * vote_average
            + vote_count_weight * vote_count
            + revenue_weight * revenue
            + recency_weight * recency
            + user_rating_weight * user_rating
            + genre_preference_weight * genre_preference_score
        )

    def _get_genre_preference_score(self):
        from django.db.models import Count

        genre_preference_score = (
            self.values("genre")
            .annotate(
                genre_count=Count("genre"),
                genre_preference_score=Cast(
                    Value(1.0) / F("genre_count"), output_field=FloatField()
                ),
            )
            .values("genre_preference_score")
        )
        return Subquery(genre_preference_score)

    def _normalize(self, field_name):
        max_value = self.aggregate(Max(field_name))[f"{field_name}__max"]
        min_value = self.aggregate(Min(field_name))[f"{field_name}__min"]
        value_range = max_value - min_value
        return ExpressionWrapper(
            (F(field_name) - min_value) / value_range, output_field=FloatField()
        )

    def get_top_movies(self, count=100, **kwargs):
        return self.annotate(ranking=self.get_ranking(**kwargs)).order_by("-ranking")[
            :count
        ]

    def get_user_recommendations(self, user_id, count=100, **kwargs):
        from movies.models import UserMoviePreference

        user_preferences = UserMoviePreference.objects.filter(user_id=user_id)
        return (
            self.annotate(ranking=self.get_ranking(**kwargs))
            .filter(id__in=user_preferences.values_list("movie_id", flat=True))
            .order_by("-ranking")[:count]
        )
