from .views import ViewCadastrarTreinamento, ViewDeletarTreinamento, ViewAtualizarTreinamento, MostrarTreinamentoViewOfc
from django.urls import path

urlpatterns = [
    path('treinamentosofc/', MostrarTreinamentoViewOfc.as_view(), name='mostrartreinamentoofc'),
    path('cadastrartreinamento/', ViewCadastrarTreinamento.as_view(), name='cadastrartreinamento'),
    path('atualizartreinamento/<int:pk>/', ViewAtualizarTreinamento.as_view(), name='atualizartreinamento'),
    path('deletartreinamento/<int:pk>/', ViewDeletarTreinamento.as_view(), name='deletartreinamento'),
  ]