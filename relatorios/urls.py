from .views import ViewCadastrarRelatorio, MostrarRelatoriosOfc, ViewDeletarRelatorios, ViewAtualizarRelatorios
from django.urls import path

urlpatterns = [
    path('relatoriosofc/', MostrarRelatoriosOfc.as_view(), name='relatoriosofc'),
    path('cadastrarrelatorio/', ViewCadastrarRelatorio.as_view(), name='cadastrarrelatorio'),
    path('atualizarrelatorio/<int:pk>/', ViewAtualizarRelatorios.as_view(), name='atualizarrelatorio'),
    path('deletarrelatorio/<int:pk>/', ViewDeletarRelatorios.as_view(), name='deletarrelatorio'),
  ]