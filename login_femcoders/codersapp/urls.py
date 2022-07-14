"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from django.contrib.auth.views import auth_login
from django.conf.urls.static import static
import login
from codersapp import views
from codersapp.views import *
from login import settings

urlpatterns = [
    path('', inicio, name='inicio'),
    path('evaluacion/', evaluacion, name='evaluacion'),
    path('evaluacion/perfilAlumno/<int:id>', perfilAlumno, name='perfilalumno'),
    path('EditarNota/<int:id>', editevau, name='ponernota'),
    path('evaluacion/<int:id>', eliminarEvau, name='eliminar'),
    path('nuevo_alumno/', nuevoAlumno, name='nuevoal'),
    path('mis_alumnos/', ListaAlumno, name='listaal'),
    path('nueva_evaluacion/', nuevaEvaluacion, name='nuevaevaluacion'),
    path('salir/', salir, name='saliendo'),
    path('registrar/', registro, name='registro'),
    path('imagen/', vistaImagen, name='imagen'),
    path('success/', success, name='success'),
    path('displayImagen/', displayImagen, name='displayImagen'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)