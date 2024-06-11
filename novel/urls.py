from django.urls import path
from .views import (
    AutorListView, AutorDetailView, AutorCreateView, AutorUpdateView, AutorDeleteView,
    NovelaListView, NovelaDetailView, NovelaCreateView, NovelaUpdateView, NovelaDeleteView,
    RecenzeListView, RecenzeDetailView, RecenzeCreateView, RecenzeUpdateView, RecenzeDeleteView, index
)

urlpatterns = [
    path('', index, name='index'),

    # Autor URLs
    path('autori/', AutorListView.as_view(), name='autor_list'),
    path('autori/<int:pk>/', AutorDetailView.as_view(), name='autor_detail'),
    path('autori/nova/', AutorCreateView.as_view(), name='autor_create'),
    path('autori/<int:pk>/edit/', AutorUpdateView.as_view(), name='autor_update'),
    path('autori/<int:pk>/delete/', AutorDeleteView.as_view(), name='autor_delete'),

    # Novela URLs
    path('novely/', NovelaListView.as_view(), name='novela_list'),
    path('novely/<int:pk>/', NovelaDetailView.as_view(), name='novela_detail'),
    path('novely/nova/', NovelaCreateView.as_view(), name='novela_create'),
    path('novely/<int:pk>/edit/', NovelaUpdateView.as_view(), name='novela_update'),
    path('novely/<int:pk>/delete/', NovelaDeleteView.as_view(), name='novela_delete'),

    # Recenze URLs
    path('novely/<int:novela_pk>/recenze/nova/', RecenzeCreateView.as_view(), name='recenze_create'),
    path('recenze/', RecenzeListView.as_view(), name='recenze_list'),
    path('recenze/<int:pk>/', RecenzeDetailView.as_view(), name='recenze_detail'),
    path('recenze/<int:pk>/edit/', RecenzeUpdateView.as_view(), name='recenze_update'),
    path('recenze/<int:pk>/delete/', RecenzeDeleteView.as_view(), name='recenze_delete'),
]
