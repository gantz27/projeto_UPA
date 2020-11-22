from django import forms
from .models import Upa

class UpaForm(forms.ModelForm):
    class Meta:
        model = Upa
        fields = ['cep','nome','endereco','telefone','especificacoes','descricao']