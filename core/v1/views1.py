from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import permissions

from core.models import Servico, Avaliacao

from . serializer import ServicoSerializer, AvaliacaoSerializer


# class ServicoViewSet(viewsets.ModelViewSet):
#     queryset = Servico.objects.all()
#     serializer_class = ServicoSerializer
#     permission_classes = [permissions.IsAuthenticated]


class ServicoAPIView(APIView):
    """
        Api de Avaliação de Serviços    
    """
    def get(self, request):
        servicos = Servico.objects.all()
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ServicoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"mensagem": "Criado com Sucesso"}, status=status.HTTP_201_CREATED)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)




class AvaliacaoViewSet(viewsets.ModelViewSet):
    """
        Api de Avaliação de Serviços    
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer