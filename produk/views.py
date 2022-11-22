from django.shortcuts import render

# Create your views here.
def produk(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexproduk.html', konteks)