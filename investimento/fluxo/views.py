from django.views.generic import ListView,CreateView,DeleteView,UpdateView,TemplateView
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from investimento.fluxo.forms import FluxoForm
from investimento.fluxo.models import Fluxo
from django.http import JsonResponse


class ClientView(TemplateView):
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
                for i in Fluxo.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
                cli = Fluxo()
                cli.data = request.POST['data']
                cli.tipo_fluxo = request.POST['tipo']
                cli.corretora = request.POST['corretora']
                cli.valor = request.POST['valor']
                cli.save()
            elif action == 'edit':
                cli = Fluxo.objects.get(pk=request.POST['id'])
                cli.names = request.POST['names']
                cli.surnames = request.POST['surnames']
                cli.dni = request.POST['dni']
                cli.date_birthday = request.POST['date_birthday']
                cli.address = request.POST['address']
                cli.gender = request.POST['gender']
                cli.save()
            elif action == 'delete':
                cli = Fluxo.objects.get(pk=request.POST['id'])
                cli.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['list_url'] = reverse_lazy('investimento.fluxo:client')
        context['entity'] = 'Clientes'
        context['form'] = FluxoForm()
        return context
