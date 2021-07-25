from django.urls import path
from . import views
from django.conf.urls import url
from django.http import HttpResponse

urlpatterns = [
    path('',views.home, name="home"),
    path('login/',views.loginpage, name="loginpage"),
    path('logout/',views.logoutuser,name="logoutuser"),
    path('register/',views.register,name="register"),
    path('deleteMovie/<str:pk>/',views.deleteMovie,name='deleteMovie'),
    path('updateMovie/<str:pk>/',views.updateMovie,name='updateMovie')
]