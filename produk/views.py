from django.shortcuts import render, redirect
from .forms import FormProduk
from .models import produk
from django.contrib import messages




# create your views here.
def produk_list(request):
    context = {
        'daftar_produk' : Produk.objects.all()
    }
    return render(request, "produk/produk_list.html", context)

# untuk INSERT dan UPDATE
def produk_form(request, id=0):
    if request.method == 'POST':
        if id == 0:
            form = Produkform(request.POST)
        else:
            i = Produk.objects.get(pk=id)
            form = Produkform(request.POST, instance=i)
        form.save()
        return redirect ('/produk/list')
    else:
        if id ==0:
            form = ProdukForm()
        else:
            i = Produk.objects.get(pk=id)
            form = ProdukForm(instance=i)
        return render(request, "produk/produk_form.html", {'form': form})

#untuk Delete
def produk_delete(request, id):
    i = Produk.objects.get(pk=id)
    i.delete()
    return redirect ('/produk/list')