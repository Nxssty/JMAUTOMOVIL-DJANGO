from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import AutoForm, ImagenFormSet
from .models import Autos

def home(request):
    autos_list = Autos.objects.all()
    paginator = Paginator(autos_list, 9)  # Mostrar 9 autos por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'core/index.html', {'page_obj': page_obj})

def descripcion(request, id):
    auto = Autos.objects.get(id=id)
    imagenes = auto.imagenes.all()
    return render(request, 'core/descripcion.html', {'auto': auto, 'imagenes': imagenes})

def crear_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        formset = ImagenFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            auto = form.save()
            for form in formset:
                imagen = form.save(commit=False)
                imagen.auto = auto
                imagen.save()
            return redirect('home')
    else:
        form = AutoForm()
        formset = ImagenFormSet()
    return render(request, 'core/crear_auto.html', {'form': form, 'formset': formset})
