from django.shortcuts import render
from django.views.generic import ListView,DeleteView, CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.urls import reverse_lazy

from investimento.fluxo.forms import FluxoForm
from investimento.fluxo.models import Fluxo


# Create your views here.
class FluxoCreateView(CreateView,ListView):
    model = Fluxo
    form_class = FluxoForm
    template_name = 'fluxo/listar.html'
    success_url = reverse_lazy('investimento.fluxo:fluxo-list')

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Fluxo.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                flx = Fluxo()
                flx.data = request.POST['data']
                flx.tipo = request.POST['tipo']
                flx.corretora = request.POST['corretora']
                flx.valor = request.POST['valor']
                flx.save()
            else:
                data['error'] = 'Ocorreu umerro'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FluxoForm()
        return context



class FluxoListViews(ListView,CreateView):
    model = Fluxo
    template_name = 'fluxo/listar.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                position = 1
                for i in Fluxo.objects.all():
                    item = i.toJSON()
                    item['position'] = position
                    data.append(item)
                    position += 1
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Controle de fluxo'
        context['title_conteudo'] = 'Fluxo de caixa'
        context['list_url'] = reverse_lazy('website:fluxo-list')
        context['breadcrumb'] = 'Fluxo'

        return context
class FluxoDeleteViews(DeleteView):
    model = Fluxo
    success_url = reverse_lazy('investimento.fluxo:fluxo-list')
    template_name = 'fluxo  /listar.html'