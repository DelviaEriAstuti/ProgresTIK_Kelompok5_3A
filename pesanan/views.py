from django.shortcuts import render

# Create your views here.
def pesanan(request):
    judul = []

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexpesanan.html', konteks)