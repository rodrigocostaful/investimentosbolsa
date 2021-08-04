from django.urls import path

from investimento.fluxo.views import listar_fluxo

app_name = 'investimento.fluxo'


urlpatterns = [
    path('fluxo', listar_fluxo, name='listar_fluxo'),

]