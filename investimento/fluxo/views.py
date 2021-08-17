from datetime import datetime
from django.db.models import FloatField, DecimalField
from django.db.models import Sum, Value as V
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from investimento.fluxo.forms import FluxoForm
from investimento.fluxo.models import Fluxo


class ClientView(TemplateView):
    template_name = 'fluxo/listar.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'fluxo_lista_tabela':
                data = [i.toJSON() for i in Fluxo.objects.all()]
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
                data['error'] = 'há um erro     '
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def grafico_highcharts(self):
        data_en = []
        data_sd = []
        year = datetime.now().year

        for m in range(1, 13):
            for m in range(1, 13):
                # total_en = Fluxo.objects.filter(tipo_fluxo='en', data__year=year, data__month=m).aggregate(Sum('valor', 0)))
                total_en = Fluxo.objects.filter(tipo_fluxo='en',data__year=year, data__month=m).aggregate(r=Coalesce(Sum('valor'), 0, output_field=FloatField())).get('r')
                total_sd = Fluxo.objects.filter(tipo_fluxo='sd',data__year=year, data__month=m).aggregate(r=Coalesce(Sum('valor'), 0, output_field=FloatField())).get('r')
                data_en.append(float(total_en))
                data_sd.append(float(total_sd))
            return [{'name':'Entrada', 'data': data_en},{'name':'Saída', 'data': data_sd}]


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de fluxo'
        context['list_url'] = reverse_lazy('investimento.fluxo:client')
        context['entity'] = 'Fluxos'
        context['form'] = FluxoForm()
        context['entradas'] = Fluxo.objects.filter(tipo_fluxo='en').aggregate(r=Coalesce(Sum('valor'), 0, output_field=FloatField())).get('r')
        context['saida'] = Fluxo.objects.filter(tipo_fluxo='sd').aggregate(r=Coalesce(Sum('valor'), 0, output_field=FloatField())).get('r')
        context['total_fluxo'] = Fluxo.objects.filter(tipo_fluxo='en').aggregate(r=Coalesce(Sum('valor'), 0, output_field=FloatField())).get('r')-Fluxo.objects.filter(tipo_fluxo='sd').aggregate(r=Coalesce(Sum('valor'), 0, output_field=FloatField())).get('r')


        context['grafico_highcharts'] = self.grafico_highcharts()

        return context
