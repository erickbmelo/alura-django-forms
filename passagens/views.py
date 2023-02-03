from django.shortcuts import render
from passagens.forms import PassagemForms

def index(request):
    form = PassagemForms()
    return render(request, 'index.html', {'form': form})

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        return render(request, 'minha_consulta.html', {'form': form})

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        if form.is_valid():
            return render(request, 'minha_consulta.html', {'form':form})
        else:
            return render(request, 'index.html', {'form':form})