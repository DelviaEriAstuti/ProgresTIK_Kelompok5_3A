from django.shortcuts import render

# Create your views here.
def keranjang(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexkeranjang.html', konteks)