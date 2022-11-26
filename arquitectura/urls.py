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
from arquitectura.vista import  login, index, calendario, profe, tienda, prueba, editare, editalola, eliminare, form2, registrare

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tienda', tienda, name='tienda'),
    path('login', login, name='login'),
    path('', index, name='index'),
    path('index', index, name='index'),
     path('api_dote/', include('api_dote.urls')), #para que se pueda acceder a la pagina de api_lola
    path('calendario', calendario, name='calendario'),
    path('profe', profe, name='profe'),
     path('form2', form2, name='form2'), #para que se pueda acceder a la pagina de index
    path('prueba', prueba, name='prueba'),
     path('editare/<id>', editare, name='editare'), #para que se pueda acceder a la pagina de editar
    path('editalola', editalola, name='editalola'), #para que se pueda acceder a la pagina de editar
    path('eliminare/<id>', eliminare, name='eliminare'), #para que se pueda acceder a la pagina de eliminar
    path('registrare', registrare, name='registrare'), #para que se pueda acceder a la pagina de registrar
]

