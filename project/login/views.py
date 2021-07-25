from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Movie
from .forms import RegisterForm, MovieForm
from .filters import MovieFilter


def register(request):
    if request.user.is_authenticated:
        return redirect('../')
    else:
        form = RegisterForm
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Profile Created')
                return redirect('../login')
            else:
                messages.info(request,'Something went wrong')
        context = {'form':form}
        return render(request,'login/registerpage.html',context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('../')
    else:
        if request.method=='POST':
            uname=request.POST.get('username')
            pword=request.POST.get('password')
            user = authenticate(request,username=uname,password=pword)

            if user is not None:
                login(request, user)
                return redirect('../')
            else:
                messages.info(request,'Username or Password is incorrect')

        return render(request,'login/loginpage.html')

def logoutuser(request):
    logout(request)
    messages.info(request,"Logged Out!")
    return redirect('../login')

@login_required(login_url='../login')
def home(request):
    all_movies = Movie.objects.all()


    usr = request.user.username
    form = MovieForm()

    myFilter = MovieFilter(request.GET, queryset=all_movies)
    all_movies = myFilter.qs

    if request.method == 'POST':
        post = request.POST.copy()
        post['user']=usr
        form = MovieForm(post)
        if form.is_valid:
            form.save()
    context = {'all':all_movies,'usr':usr,'form':form, 'myFilter':myFilter}
    return render(request,'login/homepage.html',context)

@login_required(login_url='../login')
def deleteMovie(request,pk):
    movie = Movie.objects.get(id=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('/')
    context = {'item':movie}
    return render(request,'login/delete.html',context)


@login_required(login_url='../login')
def updateMovie(request,pk):
    movie = Movie.objects.get(id=pk)
    form = MovieForm(instance=movie)
    usr = request.user.username
    if request.method == 'POST':
        post = request.POST.copy()
        post['user']=usr
        form = MovieForm(post)
        if form.is_valid:
            movie.delete()
            form.save()
            return redirect('/')
    context = {'item':form}
    return render(request,'login/update.html',context)