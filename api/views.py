from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer
from .services import buscar_produtos_externos


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


@api_view(['GET'])
def produtos_externos(request):
    resultado = buscar_produtos_externos()
    return Response(resultado)
