from django.shortcuts import render
from .models import EventosGe, EventosAu, Avisos, StatusAtendimento

# Create your views here.

def eventos_au(request):

    eventos_au ={
        'eventos_au': EventosAu.objects.all()
    }

    return eventos_au

def eventos_ge(request):
    eventos_ge ={
        'eventos_ge': EventosGe.objects.all()
    }

    return eventos_ge


def avisos(request):
    avisos = {
        'avisos':Avisos.objects.all()
    }
    return avisos

def status(request):
    
    status_geral = {
        'status_atendimento': StatusAtendimento.objects.all()
    }
    return status_geral

def combina(request):
    eventos_au_data = eventos_au(request)
    eventos_ge_data = eventos_ge(request)
    avisos_data = avisos(request)
    status_geral = status(request)

    context = {
        'eventos_au': eventos_au_data['eventos_au'],
        'eventos_ge': eventos_ge_data['eventos_ge'],
        'avisos': avisos_data['avisos'],
        'status_atendimento': status_geral['status_atendimento'],

    }
    return render(request, 'usuarios/index.html', context)