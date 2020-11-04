from django.urls import path
from .views import list_upa, create_upa, update_upa, delete_upa

urlpatterns = [
    path('', list_upa, name='list_crime'),
    path('new', create_upa, name'create_upa'),
    path('update/<int:id>/', update_upa, name='update_upa'),
    path('delete/<int:id>/',delete_upa, name'delete_upa'), 



]
from django import forms
from .models import Upa

class UpaForm(forms.ModelForm):
    class Meta:
        model = Upa
        fields = ['cep','endereço','nome','telefone','especificacoes','descricao']