from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . views import  AvaliacoesAPIView, ServicosAPIView, AvaliacaoAPIView, ServicoAPIView


# router = DefaultRouter()
# router.register(r'servicos', ServicoViewSet, basename='servico')
#router.register(r'servicos',ServicoAPIView.as_view(), basename='servico')
# router.register(r'avaliacoes', AvaliacaoViewSet, basename='avaliacao')
urlpatterns = [
    path('servicos/', ServicosAPIView.as_view(), name='servicos'),
    path('servicos/<int:pk>/', ServicoAPIView.as_view(), name='servico'),
    path('servicos/<int:servico_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('servicos/<int:servico_pk>/avaliacoes/<int:avaliacao_pk>/', ServicosAPIView.as_view(), name='curso_avaliacao'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),    
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
    # path('', include(router.urls))
]