from django.urls import path

from investimento.core.views import dashboard

app_name = 'investimento.core'
urlpatterns = [
    path('', dashboard, name='dashboard'),

]