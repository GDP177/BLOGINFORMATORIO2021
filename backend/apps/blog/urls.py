from django.urls import path
from . import views
from .views import DetalleNoticia, Listar, CrearNoticia, UpdateNoticia, DeleteNoticia

urlpatterns= [
	path('lista/', Listar.as_view(), name='lista'),
	path('', views.home, name='home'),
	path('<slug:pk>/detalle', DetalleNoticia.as_view(), name='detalle'),
	path('<slug:pk>/update', UpdateNoticia.as_view(), name='update'),
	path('<slug:pk>/delete', DeleteNoticia.as_view(), name='delete'),
	path('crear/', CrearNoticia.as_view(), name='crear')
]