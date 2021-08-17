from django.db import models
from django.forms import model_to_dict

# Create your models here.

class Corretora(models.Model):
    codigo = models.PositiveIntegerField()
    nome_completo = models.CharField(max_length=255, unique=True)
    nome_exibir = models.CharField(max_length=255)
    creat_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_exibir


    class Meta:
        verbose_name_plural = 'Corretoras'

class Fluxo(models.Model):
    TIPO_FLUXO_CHOICES = [
        ('en', 'Entrada'),
        ('sd', 'Saida'),
    ]
    tipo_fluxo = models.CharField(max_length=2, choices=TIPO_FLUXO_CHOICES,db_index=True)
    corretora = models.ForeignKey("Corretora", on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=19, decimal_places=2, db_index=True)
    data = models.DateField(null=False, blank=False,db_index=True)
    creat_at = models.DateTimeField(auto_now=True, verbose_name='Data',db_index=True)
    updated_at = models.DateTimeField(auto_now=True,db_index=True)

    def __str__(self):
        return self.get_tipo_fluxo_display()

    def toJSON(self):
        item = model_to_dict(self)
        item['tipo'] = self.get_tipo_fluxo_display()
        item['corretora'] = self.corretora.nome_exibir
        return item

    class Meta:
        verbose_name = 'Fluxo'
        verbose_name_plural = 'Fluxos'
        ordering = ['data']