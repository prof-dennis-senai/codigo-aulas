from rest_framework import serializers
from api.models import PessoaApi as Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'