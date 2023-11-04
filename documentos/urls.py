from .views import ViewCadastrarDocumento, ViewDeletarDocumento, ViewAtualizarDocumento, MostrarDocumentoOfc
from django.urls import path

urlpatterns = [
    path('documentosofc/', MostrarDocumentoOfc.as_view(), name='documentosofc'),
    path('cadastrardocumento/', ViewCadastrarDocumento.as_view(), name='cadastrardocumento'),
    path('atualizardocumento/<int:pk>/', ViewAtualizarDocumento.as_view(), name='atualizardocumento'),
    path('deletardocumento/<int:pk>/', ViewDeletarDocumento.as_view(), name='deletardocumento'),
  ]