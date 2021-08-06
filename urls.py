from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='bitkart'),
    path('home',views.home,name='bitkart'),
    path('register', views.register, name="bitkart"),
    path('login',views.login,name='bitkart'),

]