from django.urls import path

from investimento.fluxo.views import  FluxoListViews

app_name = 'investimento.fluxo'


urlpatterns = [
    path('fluxo/', FluxoListViews.as_view(), name='fluxo-list'),

]