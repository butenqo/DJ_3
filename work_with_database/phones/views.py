from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    
    sort_by = request.GET.get('sort')
    if sort_by == 'min_price': 
        sorted_phone = Phone.objects.order_by('price')
    if sort_by == 'max_price': 
        sorted_phone = Phone.objects.order_by('-price')
    if sort_by == 'name': 
        sorted_phone = Phone.objects.order_by('name')
    if sort_by == None: 
        sorted_phone = Phone.objects.order_by('name')
    
    context = {'phones':sorted_phone}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone':Phone.objects.get(slug=slug)}
    return render(request, template, context)
