from django.urls import path

from investimento.core.views import home

app_name = 'investimento.core'
urlpatterns = [
    path('', home),

]
