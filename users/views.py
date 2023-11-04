from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CustomUser
from django.shortcuts import render, redirect
from django.views import View
from .form import RegistrationForm, EditFormUser, RegistrationFormRH
from django.contrib.auth.models import Group
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(LoginRequiredMixin,GroupRequiredMixin,View):
    group_required = [u"rh", u"altocomando"]
    login_url = reverse_lazy('login')
    template_name = 'templates/formsoficiais.html'
    
    def get(self, request):
        form = RegistrationFormRH()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationFormRH(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = CustomUser.objects.create_user(username=username, password=password)

            group = Group.objects.get(name='praça')
            user.groups.add(group)

            return redirect('user_list')

        return render(request, self.template_name, {'form': form})


class UserListView(LoginRequiredMixin,GroupRequiredMixin,ListView):
    group_required = [u"oficial",u"rh", u"altocomando"]
    login_url = reverse_lazy('login')
    model = CustomUser
    template_name = 'templates/userlist.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q')
        queryset = CustomUser.objects.all()

        if q:
            queryset = queryset.filter(username__icontains=q)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Recupere os grupos de cada usuário e adicione-os ao contexto
        users_with_groups = []
        for user in context['users']:
            user_with_groups = {
                'user': user,
                'groups': user.groups.all(),
            }
            users_with_groups.append(user_with_groups)

        context['users_with_groups'] = users_with_groups

        user = self.request.user
        is_member_of_rh = user.groups.filter(name='rh').exists()
        is_member_of_altocomando = user.groups.filter(name='altocomando').exists()
        context['is_member_of_rh'] = is_member_of_rh
        context['is_member_of_altocomando'] = is_member_of_altocomando

        return context


class UserUpdateView(LoginRequiredMixin, GroupRequiredMixin,UpdateView):
    group_required = [u"rh", u"altocomando"]
    login_url = reverse_lazy('login')
    model = CustomUser
    form_class = EditFormUser
    template_name = 'templates/formsoficiais.html'
    success_url = reverse_lazy('user_list')

class UserUpdateViewAC(LoginRequiredMixin, GroupRequiredMixin,UpdateView):
    group_required = u"altocomando"
    login_url = reverse_lazy('login')
    model = CustomUser
    form_class = RegistrationForm
    template_name = 'templates/formsoficiais.html'
    success_url = reverse_lazy('user_list')

class UserDeleteView(LoginRequiredMixin, GroupRequiredMixin,DeleteView):
    group_required = [u"rh", u"altocomando"]
    login_url = reverse_lazy('login')
    model = CustomUser
    template_name = 'templates/deletofc.html'
    success_url = reverse_lazy('user_list')

