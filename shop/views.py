from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_page!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        prodt=products.objects.filter(categ=c_page,accessable_prodts=True)
    else:
        prodt=products.objects.all().filter(accessable_prodts=True)
    cat=category.objects.all()
    return render(request,'index.html',{'pr':prodt,'ct':cat})