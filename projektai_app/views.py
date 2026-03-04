from django.views import generic
from .models import Projektas

# Create your views here.
class ProjektasView(generic.ListView):
    model = Projektas
    context_object_name = 'all_rows'
    template_name = 'index.html'


class ProjektasDetailView(generic.DetailView):
    model = Projektas
    context_object_name = 'one_project_row'
    template_name = 'one_project.html'
