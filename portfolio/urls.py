"""
URLs de la aplicación portfolio.
"""

from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.contact_view, name='contact'),
]
