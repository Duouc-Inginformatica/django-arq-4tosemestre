"""arquitectura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
# from api.views import index
from arquitectura.vista import  login, index, calendario, profe, tienda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tienda', tienda, name='tienda'),
    path('login', login, name='login'),
    path('', index, name='index'),
    path('calendario', calendario, name='calendario'),
    path('profe', profe, name='profe'),
]
