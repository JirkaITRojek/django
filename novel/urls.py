from django.urls import path
from . import views

urlpatterns = [
    path('novel/', views.novel, name='novel'),
]