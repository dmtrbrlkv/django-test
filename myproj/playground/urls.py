from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'playground'

urlpatterns = [
    path('', views.PlaygroundIndexView.as_view(), name='index'),   
]
