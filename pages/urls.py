from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPagesView.as_view(), name='about'),
    path('service/', ServicePageView.as_view(), name='service'),
    path('contacts/', ContactPageView.as_view(), name='contacts')
]