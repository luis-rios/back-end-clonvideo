from rest_framework.routers import DefaultRouter

from espacios.views import EspacioViewSet

router = DefaultRouter()
router.register(r'/Espacio', EspacioViewSet)
urlpatterns = router.urls
