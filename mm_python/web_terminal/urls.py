from django.urls import path

from . import views

urlpatterns = [
    path('web-terminal/', views.web_terminal, name='web-terminal'),

]