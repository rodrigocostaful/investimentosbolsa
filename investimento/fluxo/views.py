from django.shortcuts import render


# Create your views here.
def listar_fluxo(request):

    data = {
        'titulo' : "Lista de fluxo"
    }

    return render(request, 'fluxo/listar.html', data)

