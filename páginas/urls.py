from .views import ViewPrincipal, ViewUniformes
from relatorios.views import MostrarRelatorios
from controledeacesso.views import AlterarSenhaView
from django.urls import path
from treinamentos.views import MostrarTreinamentoView, TreinamentosDetailView
from documentos.views import MostrarDocumento, DocumentoDetailView
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    path('principal/', ViewPrincipal.as_view(), name='principal'),
    path('configurações/', AlterarSenhaView.as_view(), name='config'),
    path('relatórios/', MostrarRelatorios.as_view(), name='relatorios'),
    path('treinamentos/', MostrarTreinamentoView.as_view(), name='treinamentos'),
    path('treinamentos/<int:pk>/', TreinamentosDetailView.as_view(), name='detalhestreinamentos'),
    path('documentos/<int:pk>/', DocumentoDetailView.as_view(), name='detalhesdocumentos'),
    path('documentos/', MostrarDocumento.as_view(), name='documentos'),
    path('uniformes/', ViewUniformes.as_view(), name='uniformes'),
]