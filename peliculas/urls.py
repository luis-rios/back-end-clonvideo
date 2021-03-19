from rest_framework.routers import DefaultRouter

from peliculas.views import PeliculaViewSet

router = DefaultRouter()
router.register(r'Pelicula/', PeliculaViewSet)
urlpatterns = router.urls
