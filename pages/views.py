from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(LoginRequiredMixin, TemplateView):
    template_name = 'about.html'

