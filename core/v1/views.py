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
            return self.filter_queryset(servico_id=self.kwargs.get('servico_id'))
        
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer    

