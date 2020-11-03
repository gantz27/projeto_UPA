from django.shortcuts import render
from .models import Upa
from .forms import UpaForm

def list_upa(request):
    upas = Upa.objects.all()
    return render(request, 'upa.html', {'upas': upas})

    def create_upa(request):
        form = UpaForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('list_upa')

        return render(request, 'upa-form.html', {'form': form})

def update_upa(request,cep):
    upa = Upa.objects.get(cep=cep)
    form = UpaForm(request.POST or None, instance=upa)

    if form.is_valid():
        form.save()
        return redirect('list_upa')

    return render (request, 'upa-form.html', {'form': form, 'upa': upa})   


def delete_upa(request, cep):
    upa = Upa.objects.get(cep=cep)

    if request.method == 'POST':
        crime.delete()
        return redirect('list_upa')

    return render(request, 'upa-delete-confirm.html', {'upa': upa})         




