from rest_framework.routers import DefaultRouter

from usuarios.views import UsuarioViewSet

router = DefaultRouter()
router.register(r'Usuario/', UsuarioViewSet)
#LLamo las urlpatterns para que esta ruta pueda estar disponible para usarla en el url global del proyecto
urlpatterns = router.urls
