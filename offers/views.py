from django.shortcuts import render, get_object_or_404
from .models import Category, Offers


def offers_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Offers.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'offers/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def offers_detail(request, id, slug):
    product = get_object_or_404(Offers, id=id, slug=slug, available=True)
    return render(request, 'offers/detail.html',
                  {'product': product})


