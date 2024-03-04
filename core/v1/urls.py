from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . views import  AvaliacaosAPIView, ServicosAPIView, AvaliacaoAPIView, ServicoAPIView


# router = DefaultRouter()
# router.register(r'servicos', ServicoViewSet, basename='servico')
#router.register(r'servicos',ServicoAPIView.as_view(), basename='servico')
# router.register(r'avaliacoes', AvaliacaoViewSet, basename='avaliacao')
urlpatterns = [
    path('servicos/', ServicosAPIView.as_view(), name='servicos'),
    path('avaliacoes/', AvaliacaosAPIView.as_view(), name='avaliacoes'),
    path('servicos/<int:pk>/', ServicoAPIView.as_view(), name='servico'),
    path('avaliacoes/<int:pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
    # path('', include(router.urls))
]