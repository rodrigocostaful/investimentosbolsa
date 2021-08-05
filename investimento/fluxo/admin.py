from django.contrib import admin
from investimento.fluxo.models import Fluxo, Corretora


# Register your models here.
class CorretoraAdmin(admin.ModelAdmin):
    list_display = ('codigo','nome_exibir', 'nome_completo')
    list_filter = ('creat_at',)
admin.site.register(Corretora, CorretoraAdmin)



class FluxoAdmin(admin.ModelAdmin):
    list_display = ('corretora', 'valor', 'data')
    list_filter = ('creat_at','corretora')
admin.site.register(Fluxo, FluxoAdmin)
