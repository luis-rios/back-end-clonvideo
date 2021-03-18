from rest_framework.routers import DefaultRouter

from series.views import SerieViewSet

router = DefaultRouter()
router.register(r'/Series', SerieViewSet)
urlpatterns = router.urls
