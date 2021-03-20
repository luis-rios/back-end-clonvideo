from rest_framework.routers import DefaultRouter

from peliculas.views import PeliculaViewSet

router = DefaultRouter()
#Declaro o defino la ruta que quiero para mis peliculas
#Y Ademas cargo la clase del viewset
router.register(r'Pelicula/', PeliculaViewSet)
urlpatterns = router.urls
