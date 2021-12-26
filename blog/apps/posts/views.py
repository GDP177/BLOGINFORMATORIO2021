from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from .models import Comentario
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



class ListarPosts(LoginRequiredMixin, ListView):
	model=Post
	template_name = "posts/posts_list.html"
	context_object_name = "posts"
	def get_queryset(self):
		posts = Post.objects.all().order_by('-fecha_creacion')
		return posts

class CrearPost(CreateView):
			model = Post
			form_class=PostForm
			success_url = '/posts'
			template_name = 'posts/post_form.html'
     	

class UpdatePost(UpdateView):
		model = Post
		form_class = PostForm
		template_name = 'posts/post_update_form.html'
		success_url = '/posts'

class DeletePost(DeleteView):
	model = Post
	success_url = reverse_lazy('posts')
 


class DetallePost(LoginRequiredMixin, DetailView):
		model=Post
		template_name="posts/post_detail.html"
		def get_context_data(self, **kwargs):
					data = super().get_context_data(**kwargs)
					data['comentarios'] = Comentario.objects.all()
					return data
	

