from django.urls import path

from . import views 

urlpatterns = [
    path('', views.home,name='home'),
    path('About', views.About, name='About'),
    path('search', views.search, name='search'),  
]