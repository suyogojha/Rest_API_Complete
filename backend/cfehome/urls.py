from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/articles/', include('articles.urls')),
    path('api/search/', include('search.urls')),
    path('api/products/', include('products.urls')),
    path('api/v2/', include('cfehome.routers'))
]

# localhost:8000/api/