from rest_framework import routers
from .views import BibliotecaViewset, AutorViewset

router = routers.DefaultRouter()
router.register(r'biblioteca', BibliotecaViewset)
router.register(r'autor', AutorViewset)
urlpatterns = router.urls