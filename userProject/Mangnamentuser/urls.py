from django.urls import path
from .views import index,LogoutView,register_view,HomeView,UserListView,UserUpdateView,edit_user

urlpatterns = [
    path('', index, name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/',register_view,name="register"),
    path('home/',HomeView.as_view(),name='home'),
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/users/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),
]