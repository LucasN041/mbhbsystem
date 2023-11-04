from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url=reverse_lazy('principal'))),
    path('login/', include('controledeacesso.urls')),
    path('paginas/', include('páginas.urls')),
    path('treinamentos/', include('treinamentos.urls')),
    path('documentos/', include('documentos.urls')),
    path('controle/', include('users.urls')),
    path('relatórios/', include('relatorios.urls')),
    path('rh/', include('rh.urls')),
]
