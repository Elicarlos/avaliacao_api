from rest_framework import serializers
from core.models import Servico, Avaliacao

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'


class AvaliacaoSerializer(serializers.ModelSerializer):
    servico_id = serializers.PrimaryKeyRelatedField(queryset=Servico.objects.all())

    


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at.strftime("%d de %B de %Y, %H:%M:%S")
        representation['updated_at'] = instance.updated_at.strftime("%d de %B de %Y, %H:%M:%S")
        representation['data_avaliacao'] = instance.data_avaliacao.strftime("%d de %B de %Y, %H:%M:%S")
        return representation
    
    
    class Meta:
        # aqui posso colocar um campo que nao será apresentado em uma consulta
        # extra_kwargs = {
        #     'nome campo': {'write_only': True}
        # }
        model = Avaliacao
        fields = '__all__'