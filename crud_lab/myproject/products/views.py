from django.shortcuts import render, redirect, get_object_or_404
from .models import product
from .forms import productform

# Create your views here.
def product_list(request):
    products=product.objects.all()
    return render(request,'products/product_list.html',{'products':products})


def product_create(request):
    if request.method=='POST':
        form=productform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form=productform()
    return render(request,'products/product_form.html',{'form':form})

def product_update(request,id):
    product=get_object_or_404(product,id=id)
    if request.method=='POST':
        form=productform(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form=productform(instance=product)
    return render(request,'products/product_form.html',{'form':form})

def product_delete(request,id):
    product=get_object_or_404(product,id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request,'products/product_delete.html',{'product':product})