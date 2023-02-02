from django.shortcuts import render
from passagens.forms import PassagemForms

def index(request):
    form = PassagemForms()
    return render(request, 'index.html', {'form': form})

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        return render(request, 'minha_consulta.html', {'form': form})