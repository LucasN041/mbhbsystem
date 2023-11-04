from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from .models import Relatorios
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .form import RelatoriosFormCadastro, RelatoriosOfcFormCadastro
from django.utils import timezone
from braces.views import GroupRequiredMixin
from django.db.models import Q


class MostrarRelatorios(GroupRequiredMixin,LoginRequiredMixin, ListView):
    group_required = [u"praça", u"oficial"]
    login_url = reverse_lazy('login')
    model = Relatorios
    template_name = 'templates/relatorios.html'
    context_object_name = 'relatorios'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['relatorios'] = Relatorios.objects.filter(treinador=self.request.user).order_by('-data_preenchimento')
        return context


class MostrarRelatoriosOfc(GroupRequiredMixin,LoginRequiredMixin, ListView):
    group_required = u"oficial"
    login_url = reverse_lazy('login')
    model = Relatorios
    template_name = 'templates/relatoriosofc.html'
    context_object_name = 'relatorios'
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q')
        queryset = Relatorios.objects.all()

        if q:
            queryset = queryset.filter(
                Q(data1__icontains=q) |
                Q(treinador__username__icontains=q) |
                Q(treinamento__icontains=q)
            )

        queryset = queryset.order_by('-data_preenchimento')

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        is_member_of_rh = user.groups.filter(name='rh').exists()
        is_member_of_altocomando = user.groups.filter(name='altocomando').exists()
        context['is_member_of_rh'] = is_member_of_rh
        context['is_member_of_altocomando'] = is_member_of_altocomando
        return context


class ViewCadastrarRelatorio(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    group_required = [u"praça", u"oficial"]
    login_url = reverse_lazy('login')
    model = Relatorios
    template_name = 'templates/forms.html'
    form_class = RelatoriosFormCadastro
    success_url = reverse_lazy('relatorios')

    def form_valid(self, form):
        usuario_logado = self.request.user

        form.instance.treinador = usuario_logado

        form.instance.data_preenchimento = timezone.now()


        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Formulário para cadastro de relatório!"
        context['botao'] = "Enviar"
        return context
    
class ViewDeletarRelatorios(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    group_required = [u"altocomando" , u"rh"]
    login_url = reverse_lazy('login')
    model = Relatorios
    template_name = 'templates/deletofc.html'
    success_url = reverse_lazy('relatoriosofc')

class ViewAtualizarRelatorios(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    group_required = [u"oficial", u"altocomando", u"rh"]
    login_url = reverse_lazy('login')
    model = Relatorios
    template_name = 'templates/formsoficiais.html'
    form_class = RelatoriosOfcFormCadastro
    success_url = reverse_lazy('relatoriosofc')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Formulário para edição de relatórios"
        context['botao'] = "Salvar"

        return context