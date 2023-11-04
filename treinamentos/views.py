from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Treinamentos 
from django.views import View
from .form import TreinamentosFormCadastro
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from braces.views import GroupRequiredMixin


# Create your views here.

class ViewCadastrarTreinamento(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    group_required = [u"altocomando", u"depensino"]
    login_url = reverse_lazy('login')
    model = Treinamentos
    template_name = 'templates/formsoficiais.html'
    form_class = TreinamentosFormCadastro
    success_url = reverse_lazy('mostrartreinamentoofc')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Formulário para cadastro de treinamentos"
        context['botao'] = "Cadastrar"

        return context
    
class ViewAtualizarTreinamento(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    group_required = [u"altocomando" , u"depensino"]
    login_url = reverse_lazy('login')
    model = Treinamentos
    template_name = 'templates/formsoficiais.html'
    form_class = TreinamentosFormCadastro
    success_url = reverse_lazy('mostrartreinamentoofc')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Formulário para edição de treinamentos"
        context['botao'] = "Salvar"

        return context
    
class ViewDeletarTreinamento(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    group_required = [u"altocomando" , u"depensino"]
    login_url = reverse_lazy('login')
    model = Treinamentos
    template_name = 'templates/deletofc.html'
    success_url = reverse_lazy('mostrartreinamentoofc')

class MostrarTreinamentoView(GroupRequiredMixin,LoginRequiredMixin,ListView):
    group_required = [u"praça", u"oficial"]
    login_url = reverse_lazy('login')
    model = Treinamentos
    template_name = 'templates/treinamentos.html'
    context_object_name = 'treinamentos'

class MostrarTreinamentoViewOfc(GroupRequiredMixin,LoginRequiredMixin,ListView):
    group_required = [u"praça", u"oficial"]
    login_url = reverse_lazy('login')
    model = Treinamentos
    template_name = 'templates/treinamentoofc.html'
    context_object_name = 'treinamentos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        is_member_of_rh = user.groups.filter(name='rh').exists()
        is_member_of_altocomando = user.groups.filter(name='altocomando').exists()
        context['is_member_of_rh'] = is_member_of_rh
        context['is_member_of_altocomando'] = is_member_of_altocomando
        return context


class TreinamentosDetailView(GroupRequiredMixin,LoginRequiredMixin,DetailView):
    group_required = [u"praça", u"oficial"]
    login_url = reverse_lazy('login')
    model = Treinamentos
    template_name = 'templates/exibirtreinamento.html'
    context_object_name = 'treinamento'
