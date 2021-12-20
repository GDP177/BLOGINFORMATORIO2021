from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Noticia
from .forms import NoticiaForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


class Listar(LoginRequiredMixin, ListView):
	login_url = 'login'
	model=Noticia
	template_name = "listar_noticias.html"
	context_object_name = "noticias"
	def get_queryset(self):
		noticias = Noticia.objects.all().order_by('-fecha_creacion')
		return noticias

@login_required(login_url='login')
def home(request):
	return render(request, 'home.html', {})


class DetalleNoticia(DetailView):
	model=Noticia
	template_name="detalle_noticia.html"

class CrearNoticia(CreateView):
	model=Noticia
	success_url='/lista'
	fields= ['autor', 'titulo','contenido']

class UpdateNoticia(UpdateView):
	model = Noticia
	form_class = NoticiaForm
	template_name = 'blog/blog_update_form.html'
	success_url='/lista'

class DeleteNoticia(DeleteView):
	model = Noticia
	success_url = reverse_lazy('lista')








