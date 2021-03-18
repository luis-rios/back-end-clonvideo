from rest_framework.routers import DefaultRouter

router = DefaultRouter
router.register(r'Pelicula', PeliculaViewSet)
urlpatterns = router.urls
