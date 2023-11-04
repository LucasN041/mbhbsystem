from django.urls import path
from .views import AdicionarUsuarioGrupoView, MostrarRequerimentoRH, ViewCadastrarRequerimento, ViewDeletarRequerimento, ViewAtualizarRequerimento

urlpatterns = [
    path('requerimentorh/', MostrarRequerimentoRH.as_view(), name='requerimentorh'),
    path('cadastrarrequerimento/', ViewCadastrarRequerimento.as_view(), name='cadastrarrequerimento'),
    path('atualizarrequerimento/<int:pk>/', ViewAtualizarRequerimento.as_view(), name='atualizarrequerimento'),
    path('deletarrequerimento/<int:pk>/', ViewDeletarRequerimento.as_view(), name='deletarrequerimento'),
    path('adicionarmilitargrupo/', AdicionarUsuarioGrupoView.as_view(), name='adicionarmilitargrupo'),

  ]