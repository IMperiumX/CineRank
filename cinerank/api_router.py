from movies.api.views import MovieViewSet

from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf import settings

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("movies", MovieViewSet)


app_name = "api"
urlpatterns = router.urls
