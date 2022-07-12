from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from codersapp.forms import *
from codersapp.models import *



#@login_required
def inicio(request):
    profesor = Profesor.objects.all()
    return render(request, 'inicio.html', {'profesor': profesor})

#@login_required
def evaluacion(request):
    laevaluacion = Evaluacion.objects.all
    laevaluacionalumno = Alumno.objects.all()

    return render(request, 'evaluacion.html', {'evaluacion': laevaluacion, 'evaalumn':laevaluacionalumno})

def cuentas(request):
    return render(request, 'login.html')

#@login_required
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


"""def salir(request):
    logout(request)
    return redirect('login/')"""


def nuevoAlumno(request):
    if request.method == 'POST':
        formaAlumno = AlumnoForm(request.POST)
        if formaAlumno.is_valid():
            formaAlumno.save()
            return redirect('listaal')
    else:
        formaAlumno = AlumnoForm

    return render(request, 'nuevoAlumno.html', {'formaAlumno': formaAlumno})

@login_required
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
