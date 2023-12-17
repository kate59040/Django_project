from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Blog
from django.shortcuts import render, redirect
from .forms import BlogPostForm


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def hello(request):
    return HttpResponse('Hello, world')


def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


@login_required
def fill(request):
    blog = Blog(title='IDK', date='2007-02-10', author='me')
    blog.save()
    return HttpResponse("Успешно")


def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, 'create_blogpost.html', {'form': form})


def read_blog(request, blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    result = f'{blog.title},  {blog.date},   {blog.author} '
    return HttpResponse(result)


def delete_blogpost(request, post_id):
    blogpost = Blog.objects.get(id=post_id)
    blogpost.delete()
    return redirect('home')


def home(request):
    blogposts = Blog.objects.all()
    result = {'blogposts': blogposts}
    return render(request, 'home.html', result)


def blogpost_list(request):
    blogposts = {'posts': Blog.objects.order_by('-date')}
    return render(request, 'blog_post.html', blogposts)
