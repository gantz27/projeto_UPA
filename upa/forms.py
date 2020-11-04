from django import forms
from .models import Upa

class UpaForm(forms.ModelForm):
    class Meta:
        model = Upa
        fields = ['cep','endereço','nome','telefone','especificacoes','descricao']