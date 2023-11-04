from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Documentos
from braces.views import GroupRequiredMixin
from django.views import View
from .form import DocumentosFormCadastro
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView


class ViewCadastrarDocumento(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    group_required = u"altocomando"
    login_url = reverse_lazy('login')
    model = Documentos
    template_name = 'templates/formsoficiais.html'
    form_class = DocumentosFormCadastro
    success_url = reverse_lazy('documentosofc')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Formulário para cadastro de documentos"
        context['botao'] = "Cadastrar"

        return context
    
class ViewAtualizarDocumento(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    group_required = u"altocomando"
    login_url = reverse_lazy('login')
    model = Documentos
    template_name = 'templates/formsoficiais.html'
    form_class = DocumentosFormCadastro
    success_url = reverse_lazy('documentosofc')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Formulário para edição de documentos"
        context['botao'] = "Salvar"

        return context
    
class ViewDeletarDocumento(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    group_required = u"altocomando"
    login_url = reverse_lazy('login')
    model = Documentos
    template_name = 'templates/deletofc.html'
    success_url = reverse_lazy('documentosofc')


class MostrarDocumentoOfc(LoginRequiredMixin, GroupRequiredMixin,ListView):
    group_required = u"oficial"
    login_url = reverse_lazy('login')
    model = Documentos
    template_name = 'templates/documentosofc.html'
    context_object_name = 'documentos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        is_member_of_rh = user.groups.filter(name='rh').exists()
        is_member_of_altocomando = user.groups.filter(name='altocomando').exists()
        context['is_member_of_rh'] = is_member_of_rh
        context['is_member_of_altocomando'] = is_member_of_altocomando
        return context


class MostrarDocumento(GroupRequiredMixin,LoginRequiredMixin,ListView):
    group_required = [u"praça", u"oficial"]
    login_url = reverse_lazy('login')
    model = Documentos
    template_name = 'templates/documentos.html'
    context_object_name = 'documentos'

class DocumentoDetailView(GroupRequiredMixin,LoginRequiredMixin,DetailView):
    group_required = [u"praça", u"oficial"]
    login_url = reverse_lazy('login')
    model = Documentos
    template_name = 'templates/exibirdocumento.html'
    context_object_name = 'documento'

