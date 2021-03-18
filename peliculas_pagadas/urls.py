from rest_framework.routers import DefaultRouter

from peliculas_pagadas.views import Pelicula_pagadaViewSet

router = DefaultRouter()
router.register(r'/Pelicula_pagada', Pelicula_pagadaViewSet)
urlpatterns = router.urls
