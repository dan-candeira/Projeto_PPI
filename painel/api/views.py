# rest_framework
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser

# serializers
from api import serializers

# models 
from api.models import Categoria, Senha, Tipo, Fila


class SenhaViewSet(viewsets.GenericViewSet, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    """Gerenciando as senhas no banco de dados"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Senha.objects.all()
    serializer_class = serializers.SenhaSerializer
    parser_classes = (MultiPartParser, JSONParser, FormParser,)
    
    def perform_create(self, serializer):
        """Criando uma nova senha"""
        serializer.save()


class CategoriaViewSet(viewsets.GenericViewSet, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    """Vizualizando categorias"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer


class TipoViewSet(viewsets.GenericViewSet, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    """Vizualizando tipos"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tipo.objects.all()
    serializer_class = serializers.TipoSerializer


class FilaViewSet(viewsets.GenericViewSet, 
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    
    """Vizualizando a fila de senhas"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Fila.objects.all()
    serializer_class = serializers.FilaSerializer