from dataclasses import fields
from django.forms import ModelForm
from django import forms 
from .models import produk

class FormProduk(ModelForm):
    class Meta: 
        model = produk
        fields = '__all__'

