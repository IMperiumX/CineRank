from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from movies.api.views import (
    CollectionViewSet,
    GenreViewSet,
    LanguageViewSet,
    MovieViewSet,
    ProductCompanyViewSet,
    ProductCountryViewSet,
)

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register(r"genres", GenreViewSet)
router.register(r"collections", CollectionViewSet)
router.register(r"languages", LanguageViewSet)
router.register(r"product_countries", ProductCountryViewSet)
router.register(r"product_companies", ProductCompanyViewSet)
router.register(r"movies", MovieViewSet)

app_name = "api"
urlpatterns = router.urls
