from rest_framework import viewsets
from api.api.serializer import PessoaSerializer
from api.models import PessoaApi as Pessoa
class PessoaViewSet(viewsets.ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = Pessoa.objects.all()