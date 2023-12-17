from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogpost/', views.blogpost_list, name='blogpost'),
    path('fill/', views.fill, name='fill'),
    path('read/<int:blog_id>/', views.read_blog, name='read'),
    path('login/', views.user_login, name='login'),
    path('delete_blogpost/<int:post_id>/', views.delete_blogpost, name='delete_blogpost'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.user_registration, name='registration'),
    path('create_blogpost/', views.create_blogpost, name='create_blogpost'),

]
