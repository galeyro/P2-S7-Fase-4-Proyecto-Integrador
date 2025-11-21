from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Alumno
import json

# Create your views here.

def index(request):
    alumnos = Alumno.objects.all()
    return render(request, 'index.html', {'alumnos': alumnos})

def crear_alumno(request):
    if request.method == 'POST':
        try:
            alumno = Alumno(
                nombre=request.POST.get('nombre'),
                apellido=request.POST.get('apellido'),
                fecha_nacimiento=request.POST.get('fecha_nacimiento') or None,
                lugar_nacimiento=request.POST.get('lugar_nacimiento') or None,
                direccion=request.POST.get('direccion') or None,
                telefono_alumno=request.POST.get('telefono_alumno') or None,
                info_escolar=request.POST.get('info_escolar') or None,
                info_salud=request.POST.get('info_salud') or None,
            )
            alumno.save()
            return JsonResponse({'success': True, 'message': 'Alumno creado exitosamente'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)

def editar_alumno(request, id):
    if request.method == 'POST':
        try:
            alumno = get_object_or_404(Alumno, id_alumno=id)
            alumno.nombre = request.POST.get('nombre')
            alumno.apellido = request.POST.get('apellido')
            alumno.fecha_nacimiento = request.POST.get('fecha_nacimiento') or None
            alumno.lugar_nacimiento = request.POST.get('lugar_nacimiento') or None
            alumno.direccion = request.POST.get('direccion') or None
            alumno.telefono_alumno = request.POST.get('telefono_alumno') or None
            alumno.info_escolar = request.POST.get('info_escolar') or None
            alumno.info_salud = request.POST.get('info_salud') or None
            alumno.save()
            return JsonResponse({'success': True, 'message': 'Alumno actualizado exitosamente'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    elif request.method == 'GET':
        alumno = get_object_or_404(Alumno, id_alumno=id)
        data = {
            'id_alumno': alumno.id_alumno,
            'nombre': alumno.nombre,
            'apellido': alumno.apellido,
            'fecha_nacimiento': alumno.fecha_nacimiento.strftime('%Y-%m-%d') if alumno.fecha_nacimiento else '',
            'lugar_nacimiento': alumno.lugar_nacimiento or '',
            'direccion': alumno.direccion or '',
            'telefono_alumno': alumno.telefono_alumno or '',
            'info_escolar': alumno.info_escolar or '',
            'info_salud': alumno.info_salud or '',
        }
        return JsonResponse(data)
    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)

def eliminar_alumno(request, id):
    if request.method == 'POST':
        try:
            alumno = get_object_or_404(Alumno, id_alumno=id)
            alumno.delete()
            return JsonResponse({'success': True, 'message': 'Alumno eliminado exitosamente'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)
