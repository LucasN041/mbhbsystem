from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser
from braces.views import GroupRequiredMixin
from django.shortcuts import render

class ViewPrincipal(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    group_required = [u"praça", u"oficial"]
    login_url = reverse_lazy('login')
    template_name = 'templates/principal.html'

    def get(self, request, *args, **kwargs):
        search_term = request.GET.get('search', '') 
        users = CustomUser.objects.filter(username__icontains=search_term) if search_term else None

        is_member_of_oficial = request.user.groups.filter(name='oficial').exists()

        context = {
            'users': users,
            'is_member_of_oficial': is_member_of_oficial,
        }
        return self.render_to_response(context)

        