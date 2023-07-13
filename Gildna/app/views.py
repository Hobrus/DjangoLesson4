from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


# Create your views here.

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'product_edit.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    context = {}
    context['products'] = products
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    # product = Product.objects.get(pk=pk)
    product = Product.objects.filter(pk=pk).first()
    context = {}
    context['product'] = product
    return render(request, 'product_detail.html', context)
