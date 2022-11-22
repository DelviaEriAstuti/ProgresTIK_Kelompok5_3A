from django.shortcuts import render

# Create your views here.
def saldo(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexsaldo.html', konteks)