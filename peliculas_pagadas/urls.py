from rest_framework.routers import DefaultRouter

from peliculas_pagadas.views import Pelicula_pagadaViewSet

router = DefaultRouter()
#Declaro o defino la ruta que quiero para mis peliculas_pagadas
#Y Ademas cargo la clase del viewset
router.register(r'Pelicula_pagada/', Pelicula_pagadaViewSet)
urlpatterns = router.urls
