from django.shortcuts import render, redirect
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

def update_upa(request,id):
    upa = Upa.objects.get(id=id)
    form = UpaForm(request.POST or None, instance=upa)

    if form.is_valid():
        form.save()
        return redirect('list_upa')

    return render (request, 'upa-form.html', {'form': form, 'upa': upa})   


def delete_upa(request, id):
    upa = Upa.objects.get(id=id)

    if request.method == 'POST':
        crime.delete()
        return redirect('list_upa')

    return render(request, 'upa-delete-confirm.html', {'upa': upa})         




