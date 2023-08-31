from rest_framework import routers
from .views import ToDoListViewset, PessoaViewset

router = routers.DefaultRouter()
router.register(r'todo', ToDoListViewset)
router.register(r'pessoa', PessoaViewset)
urlpatterns = router.urls