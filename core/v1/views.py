from rest_framework import generics
from core.models import Avaliacao, Servico
from . serializer import AvaliacaoSerializer, ServicoSerializer


class ServicosAPIView(generics.ListCreateAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer


class ServicoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer


class AvaliacaosAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer    

