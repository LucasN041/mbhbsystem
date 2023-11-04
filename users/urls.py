from django.urls import path
from .views import UserListView, RegisterView, UserUpdateView, UserDeleteView, UserUpdateViewAC

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/add/', RegisterView.as_view(), name='user_add'),
    path('users/edit/<int:pk>/', UserUpdateView.as_view(), name='user_edit'),
    path('users/editac/<int:pk>/', UserUpdateViewAC.as_view(), name='user_editac'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]
