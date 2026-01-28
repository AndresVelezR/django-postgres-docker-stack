from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_usuario', '').strip()
        
        # Validar campo vacío
        if not nombre:
            messages.error(request, 'El nombre de usuario no puede estar vacío')
        # Validar duplicados
        elif Usuario.objects.filter(nombre_usuario=nombre).exists():
            messages.error(request, f'El usuario "{nombre}" ya existe')
        # Crear usuario
        else:
            Usuario.objects.create(nombre_usuario=nombre)
            messages.success(request, f'Usuario "{nombre}" creado exitosamente')
            return redirect('crear_usuario')
    
    # Obtener todos los usuarios
    usuarios = Usuario.objects.all()
    
    return render(request, 'usuarios/formulario.html', {
        'usuarios': usuarios
    })
