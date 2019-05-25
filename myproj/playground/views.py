from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class PlaygroundIndexView(TemplateView):
    template_name = 'playground/index.html'
