from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class ListarPosts(ListView):
	model=Post
	template_name = "posts/posts_list.html"
	context_object_name = "posts"
	def get_queryset(self):
		posts = Post.objects.all().order_by('-fecha_creacion')
		return posts



class DetallePost(DetailView):
	model=Post
	template_name="posts/post_detail.html"
