from django.shortcuts import render, redirect, get_object_or_404
from .models import Nota

def index(request):
    if request.method == 'POST':
        # Si es POST, es para añadir una nueva nota
        contenido_nota = request.POST.get('nota_contenido')
        if contenido_nota:
            Nota.objects.create(contenido=contenido_nota)
        return redirect('notas_index')

    # Si es GET, muestra todas las notas
    notas = Nota.objects.all().order_by('-fecha_creacion')
    return render(request, 'app_notas/index.html', {'notas': notas})

def eliminar_nota(request, nota_id):
    # Obtiene la nota por su ID o devuelve un 404 si no existe
    nota = get_object_or_404(Nota, id=nota_id)
    if request.method == 'POST':
        nota.delete() # Elimina la nota
    return redirect('notas_index') # Redirige a la lista principal