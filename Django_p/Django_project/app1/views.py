from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect,get_object_or_404
from .forms import BlogPostForm
from .models import Blog
from datetime import datetime


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


def create_blogpost(request):
    result = {'error_message': 'Вы не вошли в акканунт.'}
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogPostForm(request.POST)
            if form.is_valid():
                blogpost = form.save(commit=False)
                blogpost.date = datetime.now()
                blogpost.author = request.user
                blogpost.save()
                return redirect('home')
        else:
            form = BlogPostForm()
        return render(request, 'create_blogpost.html', {'form': form})
    else:
        return render(request, 'error.html', result)


def delete_blogpost(request, blogpost_id):
    blogpost = get_object_or_404(Blog, id=blogpost_id)
    result = {'error_message': 'Вы не автор данного поста'}
    if request.user.is_authenticated and blogpost.author.id == request.user.id:
        blogpost.delete()
        return redirect('home')
    else:
        return render(request, 'error.html', result)


def home(request):
    blogposts = Blog.objects.all()
    result = {'blogposts': blogposts}
    return render(request, 'home.html', result)


def update_blogpost(request, blogpost_id):
    blogpost = get_object_or_404(Blog, id=blogpost_id)
    result = {'error_message': 'Вы не автор данного поста'}
    if request.user.is_authenticated and blogpost.author.id == request.user.id:
        if request.method == 'POST':
            form = BlogPostForm(request.POST, instance=blogpost)
            if form.is_valid():
                form.save()
                return redirect('home', id=blogpost_id)
        else:
            form = BlogPostForm(instance=blogpost)
        return render(request, 'update_blogpost.html', {'form': form})

    else:
        return render(request, 'error.html', result)
