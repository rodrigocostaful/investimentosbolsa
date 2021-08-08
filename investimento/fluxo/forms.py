from django.forms import *

from investimento.fluxo.models import Fluxo


class FluxoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     self.fields['data'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Fluxo
        fields = ['data', 'tipo_fluxo', 'corretora', 'valor']
        labels = {
            'Data', 'Tipo fluxo', 'Corretora', 'Valor'
        }
        widgets = {
            'data': TextInput(
                attrs={

                    'placeholder': '02/02/1990',
                    'id': 'datepicker'

                }
            ),
            'tipo_fluxo': Select(
                attrs={


                }
            ),
            'corretora': Select(
                attrs={

                }
            ),
            'valor': TextInput(
                attrs={

                }
            )

        }

