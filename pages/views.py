from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPagesView(TemplateView):
    template_name = 'about.html'


class ServicePageView(TemplateView):
    template_name = 'services.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'