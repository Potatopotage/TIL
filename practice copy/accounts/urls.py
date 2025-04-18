from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('user_update/', views.user_update, name='user_update'),
    path('delete/', views.delete, name='delete'),
]