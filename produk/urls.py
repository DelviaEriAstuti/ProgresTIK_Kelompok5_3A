from django.urls import path 
from .import views

urlpatterns = [ 
    path('', views.produk_form, name='tambah_produk'),
    path('<int:id>/', views.produk_form, name='ubah_produk'),
    path('delete/<int:id>/', views.produk_delete, name='hapus_produk'),
    path('list/', views.produk_list, name='tampil_produk'),
]