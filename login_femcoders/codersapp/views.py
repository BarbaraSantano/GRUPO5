from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

from codersapp.forms import *
from codersapp.models import *



@login_required
def inicio(request):
    profesor = Profesor.objects.all()
    materias = Materia.objects.all()
    return render(request, 'inicio.html', {'profesor': profesor, 'materia': materias})


def evaluacion(request):
    laevaluacion = Evaluacion.objects.all
    laevaluacionalumno = Alumno.objects.all()

    return render(request, 'evaluacion.html', {'evaluacion': laevaluacion, 'evaalumn':laevaluacionalumno})

def cuentas(request):
    return render(request, 'login.html')


def perfilAlumno(request, id):
    elperfilAlumno= Alumno.objects.get(pk=id)
    return render(request, 'perfilAlumno.html', {'alumno': elperfilAlumno})


def editevau(request, id):
    Notaasig = get_object_or_404(Evaluacion, pk=id)
    if request.method == 'POST':
        Notaasi = EvaluacionForm(request.POST, instance=Notaasig)
        if Notaasi.is_valid():
            Notaasi.save()
            return redirect('evaluacion')
    else:
        Notaasi = EvaluacionForm
    return render(request, 'EditarNota.html', {'nota': Notaasi})

def eliminarEvau(request, id):
    nota = get_object_or_404(Evaluacion, pk=id)
    if nota:
        nota.delete()
    return redirect('evaluacion')


def salir(request):
    logout(request)
    return redirect('/')


def nuevoAlumno(request):
    if request.method == 'POST':
        formaAlumno = AlumnoForm(request.POST)
        if formaAlumno.is_valid():
            formaAlumno.save()
            return redirect('listaal')
    else:
        formaAlumno = AlumnoForm

    return render(request, 'nuevoAlumno.html', {'formaAlumno': formaAlumno})

#@login_required
def ListaAlumno(request):
    MisAlumnos= Alumno.objects.all
    return render(request, 'listaAlumnos.html', {'Misalumnos': MisAlumnos})

def nuevaEvaluacion(request):
    if request.method == 'POST':
        formaNuevaEvaluacion = NuevaEvaluacionForm(request.POST)
        if formaNuevaEvaluacion.is_valid():
            formaNuevaEvaluacion.save()
            return redirect('evaluacion')
    else:
        formaNuevaEvaluacion = NuevaEvaluacionForm

    return render(request, 'nuevaEvaluacion.html', {'formaNuevaEvaluacion': formaNuevaEvaluacion})


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/registrar.html', context)


def vistaImagen(request):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('listaal')
    else:
        form = ImagenForm()
    return render(request, 'imagen.html', {'form': form})

def success(request):
    return HttpResponse('La imagen ha sido subida correctamente')


def displayImagen(request, id):
    imagen = Alumno.objects.get(pk=id)

    return render(request, 'displayImagen.html',
                       {'imagen': imagen})
