
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from braces.views import GroupRequiredMixin
from django.db.models import Q
from .models import Requerimento
from .form import RequerimentoForm, RequerimentoFormRH
from django.views.generic import FormView
from django.urls import reverse_lazy
from .form import AdicionarUsuarioGrupoForm
from .models import CustomUser
from django.contrib.auth.models import Group




class AdicionarUsuarioGrupoView(LoginRequiredMixin,GroupRequiredMixin,FormView):
    group_required = [u"rh", u"altocomando"]
    login_url = reverse_lazy('login')
    form_class = AdicionarUsuarioGrupoForm
    template_name = 'templates/formsoficiais.html'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        usuario = form.cleaned_data['usuario']
        grupo = form.cleaned_data['grupo']
        usuario.groups.add(grupo)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = CustomUser.objects.all()
        context['groups'] = Group.objects.all()
        return context

class MostrarRequerimentoRH(GroupRequiredMixin,LoginRequiredMixin, ListView):
    group_required = [u"rh", u"altocomando"]
    login_url = reverse_lazy('login')
    model = Requerimento
    template_name = 'templates/rh.html'
    context_object_name = 'requerimentos'
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q')
        queryset = Requerimento.objects.all()

        if q:
            queryset = queryset.filter(
                Q(solicitante__username__icontains=q) |
                Q(opcoes__icontains=q)
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

class ViewCadastrarRequerimento(GroupRequiredMixin,LoginRequiredMixin, CreateView):
    group_required = u"oficial"
    login_url = reverse_lazy('login')
    model = Requerimento
    template_name = 'templates/formsoficiais.html'
    form_class = RequerimentoForm
    success_url = reverse_lazy('cadastrarrquerimento')

    def form_valid(self, form):
        usuario_logado = self.request.user

        form.instance.solicitante = usuario_logado

        form.instance.data_preenchimento = timezone.now()


        return super().form_valid(form)
    

class ViewDeletarRequerimento(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    group_required = [u"altocomando" , u"rh"]
    login_url = reverse_lazy('login')
    model = Requerimento
    template_name = 'templates/deletofc.html'
    success_url = reverse_lazy('requerimentorh')

class ViewAtualizarRequerimento(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    group_required = [u"altocomando" , u"rh"]
    login_url = reverse_lazy('login')
    model = Requerimento
    template_name = 'templates/formsoficiais.html'
    form_class = RequerimentoFormRH
    success_url = reverse_lazy('requerimentorh')