from django.shortcuts import render
from passagens.forms import PassagemForms

def index(request):
    form = PassagemForms()
    return render(request, 'index.html', {'form': form})