from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import ProdutoViewSet, CategoriaViewSet, produtos_externos

router = DefaultRouter()

router.register(r'produtos', ProdutoViewSet)
router.register(r'categorias', CategoriaViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('produtos-externos/', produtos_externos),
]