from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'name':
        context = {
            'phones': Phone.objects.all().order_by('name')
        }
    elif sort == 'min_price':
        context = {
            'phones': Phone.objects.all().order_by('price')
        }
    elif sort == 'max_price':
        context = {
            'phones': Phone.objects.all().order_by('-price')
        }
    else:
        context = {
            'phones': Phone.objects.all()
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
