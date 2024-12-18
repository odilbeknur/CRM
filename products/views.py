from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, MeasurementForm
from django.contrib import messages
from .models import Product, Measurement


def product_list(request):
    products = Product.objects.all()
    return render(
            request, 
            'products/product_list.html', 
            {
                'products': products,
                'section': 'products'
            }
        )

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    else:
        form = ProductForm()
    return  render(request, 
                  'products/product_form.html', 
                  {
                    'form': form,
                    'section': 'products'
                }
            )

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(
            request, 
            'products/product_detail.html', 
            {
                'product': product,
                'section': 'products'
            }
        )

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    else:
        form = ProductForm(instance=product)
    return render(request, 
                  'products/product_edit.html', 
                  {
                      'form': form,
                      'section': 'products'
                    }
                )

def measurement_list(request):
    measurements = Measurement.objects.all()
    return render(
            request, 
            'measurements/measurement_list.html', 
            {
                'measurements': measurements,
                'section': 'measurements'
            }
        )
    
def measurement_create(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Замер успешно создан.')
            return redirect('measurement_list') 
    else:
        form = MeasurementForm()
    return render(
        request, 
        'measurements/measurement_form.html', 
        {
            'form': form,
            'section': 'measurements'
        }
    )

def measurement_edit(request, pk):
    measurement = get_object_or_404(Measurement, pk=pk)
    if request.method == 'POST':
        form = MeasurementForm(request.POST, request.FILES, instance=measurement)
        if form.is_valid():
            form.save()
            messages.success(request, 'Замер успешно обновлен.')
            return redirect('measurement_list') 
    else:
        form = MeasurementForm(instance=measurement)
    return render(
        request, 
        'measurements/measurement_form.html', 
        {'form': form, 'measurement': measurement}
    )