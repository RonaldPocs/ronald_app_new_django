from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

#paths arranged alphabetically by name
app_name = 'myapp'
urlpatterns = [ 
    path('Me', views.MeView.as_view(), name="me_view"),  
]