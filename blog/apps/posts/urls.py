from django.urls import path

from . import views
from .views import DetallePost, ListarPosts, CrearPost, UpdatePost, DeletePost
urlpatterns = [
    path('', views.ListarPosts.as_view(), name='posts'),
    path('<slug:pk>', views.DetallePost.as_view(), name='detalle'),
    path('<slug:pk>/update', views.UpdatePost.as_view(), name='update'),
    path('<slug:pk>/delete', views.DeletePost.as_view(), name='delete'),
    path('<slug:pk>crear/', views.CrearPost.as_view(), name='crear'),
]