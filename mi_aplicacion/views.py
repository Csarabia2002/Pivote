from django.shortcuts import render, redirect
from .forms import OfertaTrabajoForm
from .models import OfertaTrabajo

def publicar_oferta(request):
    if request.method == 'POST':
        form = OfertaTrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ofertas')
        else:
            return render(request, 'publicar_oferta.html', {'form': form, 'error': True})
    else:
        form = OfertaTrabajoForm()
    
    return render(request, 'publicar_oferta.html', {'form': form})

def ver_ofertas(request):
    ofertas = OfertaTrabajo.objects.all()
    return render(request, 'ver_ofertas.html', {'ofertas': ofertas})
# Create your views here.
