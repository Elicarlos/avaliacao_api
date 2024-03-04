from django.shortcuts import get_object_or_404
from rest_framework import generics
from core.models import Avaliacao, Servico
from . serializer import AvaliacaoSerializer, ServicoSerializer


class ServicosAPIView(generics.ListCreateAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer


class ServicoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # subescrevendo
    def get_queryset(self):
        if self.kwargs.get('servico_id'):
            return self.filter_queryset(servico_pk=self.kwargs.get('servico_pk'))
        
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('servico_id'):
            return get_object_or_404(self.get_queryset(), serivico_id=self.kwargs.get('servico_pk'),
                                     pk=self.kwargs.get('avaliacao_pk'))

        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
