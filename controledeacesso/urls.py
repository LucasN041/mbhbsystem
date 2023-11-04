from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import LoginViewModificada

urlpatterns = [
    path('', LoginViewModificada.as_view() , name= 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]