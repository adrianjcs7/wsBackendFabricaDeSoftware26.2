from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer
from .services import buscar_produtos_externos
from drf_spectacular.utils import extend_schema


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


@extend_schema(
        description="Obter produtos de fontes externas",
        responses={200:dict}
)
@api_view(['GET'])
def produtos_externos(request):
    resultado = buscar_produtos_externos()
    return Response(resultado)
