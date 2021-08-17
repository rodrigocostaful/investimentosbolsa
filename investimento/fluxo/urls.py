from django.urls import path

from investimento.fluxo.views import ClientView

app_name = 'investimento.fluxo'



from investimento.fluxo.models import Fluxo

urlpatterns = [


    #
    path('fluxo/list/', ClientView.as_view(), name='list_fluxo'),
    #

]