from django.urls import path

from investimento.fluxo.views import FluxoListViews, FluxoDeleteViews, FluxoCreateView

app_name = 'investimento.fluxo'


urlpatterns = [
    path('fluxo/', FluxoCreateView.as_view(), name='fluxo-create'),
    path('fluxo/', FluxoListViews.as_view(), name='fluxo-list'),
    path('fluxo/<int:pk>/delete/', FluxoDeleteViews.as_view(), name='fluxo-delete'),

]