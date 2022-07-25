from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
import json
# Create your views here.

def pegar_dados_na_api_alerte(chave, data):
    return requests.get(f'https://intimacoes-api.alerte.com.br/intimacoes?chave={chave}&data_do_envio={data}')


@login_required
def tarefasView(request):
    if request.method == 'POST':
        chave = request.POST.get('chave', '')
        data = request.POST.get('data', '')
        item = [ i for i in pegar_dados_na_api_alerte(chave=chave, data=data).json()['items']]
        dados = {"dados": item}
        return render(request, 'tarefas/tarefas.html', dados)  

    else:
        return render(request, 'tarefas/tarefas.html')  