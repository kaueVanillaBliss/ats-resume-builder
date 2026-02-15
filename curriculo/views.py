from django.shortcuts import render
from .forms import CurriculoForm


def criar_curriculo(request):
    if request.method == 'POST':
        form = CurriculoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'curriculo/sucesso.html')
    else:
        form = CurriculoForm()
    
    return render(request, 'curriculo/criar.html', {'form': form})

