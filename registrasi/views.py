from django.shortcuts import render

# Create your views here.
def registrasi(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexreg.html', konteks)