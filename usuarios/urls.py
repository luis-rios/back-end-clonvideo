from rest_framework.routers import DefaultRouter

from usuarios.views import UsuarioViewSet

router = DefaultRouter()
router.register(r'Usuario/', UsuarioViewSet)
urlpatterns = router.urls
