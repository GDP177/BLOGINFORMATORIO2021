from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('posts/', include('apps.posts.urls')),
    path('', include('apps.users.urls')),
    path('admin/', admin.site.urls),
]
