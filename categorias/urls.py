from rest_framework.routers import DefaultRouter

from categorias.views import CategoriaViewSet

router = DefaultRouter()
router.register(r'Categoria/', CategoriaViewSet)
urlpatterns = router.urls
