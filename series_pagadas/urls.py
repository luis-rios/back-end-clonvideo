from rest_framework.routers import DefaultRouter

from series_pagadas.views import Serie_pagadaViewSet

router = DefaultRouter()
#Declaro o defino la ruta que quiero para mis series_pagadas
#Y Ademas cargo la clase del viewset
router.register(r'Serie_pagada/', Serie_pagadaViewSet)
urlpatterns = router.urls
