from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('delete_blogpost/<int:blogpost_id>/', views.delete_blogpost, name='delete_blogpost'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.user_registration, name='registration'),
    path('create_blogpost/', views.create_blogpost, name='create_blogpost'),
    path('update_blogpost/<int:blogpost_id>/', views.update_blogpost, name='update_blogpost')

]
