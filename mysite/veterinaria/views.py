from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dueno, Veterinario, Mascota, Consulta, Vacuna
from .forms import DuenoForm, VeterinarioForm, MascotaForm, ConsultaForm, VacunaForm

def home(request):
    return render(request, 'veterinaria/home.html')

# Dueno views
class DuenoListView(ListView):
    model = Dueno

class DuenoDetailView(DetailView):
    model = Dueno
    pk_url_kwarg = 'pk'

class DuenoCreateView(CreateView):
    model = Dueno
    form_class = DuenoForm
    success_url = reverse_lazy('dueno_list')

class DuenoUpdateView(UpdateView):
    model = Dueno
    form_class = DuenoForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('dueno_list')

class DuenoDeleteView(DeleteView):
    model = Dueno
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('dueno_list')

# Veterinario views
class VeterinarioListView(ListView):
    model = Veterinario

class VeterinarioDetailView(DetailView):
    model = Veterinario
    pk_url_kwarg = 'pk'

class VeterinarioCreateView(CreateView):
    model = Veterinario
    form_class = VeterinarioForm
    success_url = reverse_lazy('veterinario_list')

class VeterinarioUpdateView(UpdateView):
    model = Veterinario
    form_class = VeterinarioForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('veterinario_list')

class VeterinarioDeleteView(DeleteView):
    model = Veterinario
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('veterinario_list')

# Mascota views
class MascotaListView(ListView):
    model = Mascota

class MascotaDetailView(DetailView):
    model = Mascota
    pk_url_kwarg = 'pk'

class MascotaCreateView(CreateView):
    model = Mascota
    form_class = MascotaForm
    success_url = reverse_lazy('mascota_list')

class MascotaUpdateView(UpdateView):
    model = Mascota
    form_class = MascotaForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('mascota_list')

class MascotaDeleteView(DeleteView):
    model = Mascota
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('mascota_list')

# Consulta views
class ConsultaListView(ListView):
    model = Consulta

class ConsultaDetailView(DetailView):
    model = Consulta
    pk_url_kwarg = 'pk'

class ConsultaCreateView(CreateView):
    model = Consulta
    form_class = ConsultaForm
    success_url = reverse_lazy('consulta_list')

class ConsultaUpdateView(UpdateView):
    model = Consulta
    form_class = ConsultaForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('consulta_list')

class ConsultaDeleteView(DeleteView):
    model = Consulta
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('consulta_list')

# Vacuna views
class VacunaListView(ListView):
    model = Vacuna

class VacunaDetailView(DetailView):
    model = Vacuna
    pk_url_kwarg = 'pk'

class VacunaCreateView(CreateView):
    model = Vacuna
    form_class = VacunaForm
    success_url = reverse_lazy('vacuna_list')

class VacunaUpdateView(UpdateView):
    model = Vacuna
    form_class = VacunaForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('vacuna_list')

class VacunaDeleteView(DeleteView):
    model = Vacuna
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('vacuna_list')
