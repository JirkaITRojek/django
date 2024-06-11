from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Autor, Novela, Recenze
from .forms import NovelaForm, AutorForm, RecenzeForm

# Autor Views
def index(request):
    return render(request, 'index.html')

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

# Novela Views
class NovelaListView(ListView):
    model = Novela
    template_name = 'novela_list.html'

class NovelaDetailView(DetailView):
    model = Novela
    template_name = 'novela_detail.html'

class NovelaCreateView(CreateView):
    model = Novela
    form_class = NovelaForm
    template_name = 'novela_form.html'
    success_url = reverse_lazy('novela_list')

class NovelaUpdateView(UpdateView):
    model = Novela
    form_class = NovelaForm
    template_name = 'novela_form.html'
    success_url = reverse_lazy('novela_list')

class NovelaDeleteView(DeleteView):
    model = Novela
    template_name = 'novela_confirm_delete.html'
    success_url = reverse_lazy('novela_list')

# Recenze Views
class RecenzeListView(ListView):
    model = Recenze
    template_name = 'recenze_list.html'

class RecenzeDetailView(DetailView):
    model = Recenze
    template_name = 'recenze_detail.html'

class RecenzeCreateView(CreateView):
    model = Recenze
    form_class = RecenzeForm
    template_name = 'recenze_form.html'

    def form_valid(self, form):
        form.instance.novela = get_object_or_404(Novela, pk=self.kwargs['novela_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('novela_detail', kwargs={'pk': self.kwargs['novela_pk']})

class RecenzeUpdateView(UpdateView):
    model = Recenze
    form_class = RecenzeForm
    template_name = 'recenze_form.html'

    def get_success_url(self):
        return reverse_lazy('novela_detail', kwargs={'pk': self.object.novela.pk})

class RecenzeDeleteView(DeleteView):
    model = Recenze
    template_name = 'recenze_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('novela_detail', kwargs={'pk': self.object.novela.pk})
