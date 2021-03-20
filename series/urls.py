from rest_framework.routers import DefaultRouter

from series.views import SerieViewSet

router = DefaultRouter()
#Declaro o defino la ruta que quiero para mis series
#Y Ademas cargo la clase del viewset
router.register(r'Series/', SerieViewSet)
urlpatterns = router.urls
