from rest_framework.routers import DefaultRouter

from series_pagadas.views import Serie_pagadaViewSet

router = DefaultRouter()
router.register(r'/Serie_pagada', Serie_pagadaViewSet)
urlpatterns = router.urls
