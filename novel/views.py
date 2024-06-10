from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Autor, Novela, Recenze
from .forms import NovelaForm, AutorForm, RecenzeForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def novel(request):
    #template = loader.get_template('myfirst.html')
    #return HttpResponse(template.render())
    class AutorListView(ListView):
        model = Autor
        template_name = 'autor_list.html'

    class AutorDetailView(DetailView):
        model = Autor
        template_name = 'autor_detail.html'

    class AutorCreateView(CreateView):
        model = Autor
        form_class = AutorForm
        template_name = 'autor_form.html'
        success_url = reverse_lazy('autor_list')

    class AutorUpdateView(UpdateView):
        model = Autor
        form_class = AutorForm
        template_name = 'autor_form.html'
        success_url = reverse_lazy('autor_list')

    class AutorDeleteView(DeleteView):
        model = Autor
        template_name = 'autor_confirm_delete.html'
        success_url = reverse_lazy('autor_list')