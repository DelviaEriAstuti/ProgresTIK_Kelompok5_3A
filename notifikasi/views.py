from django.shortcuts import render

# Create your views here.
def notifikasi(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexnotifikasi.html', konteks)