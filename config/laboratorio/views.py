from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Laboratorio
from .forms import LaboratorioForm  # Crearemos este formulario en el paso 2.

# Vista para listar laboratorios
def laboratorio_list(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio/laboratorio_list.html', {'laboratorios': laboratorios})

# Vista para crear un laboratorio
def laboratorio_create(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laboratorio:laboratorio_list')
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorio/laboratorio_form.html', {'form': form})

# Vista para actualizar un laboratorio
def laboratorio_update(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('laboratorio:laboratorio_list')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorio/laboratorio_form.html', {'form': form})

# Vista para eliminar un laboratorio
def laboratorio_delete(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorio:laboratorio_list')
    return render(request, 'laboratorio/laboratorio_confirm_delete.html', {'laboratorio': laboratorio})